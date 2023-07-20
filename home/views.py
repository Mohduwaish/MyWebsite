from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from TechBlog.models import TechPost
from home.models import Contact,Slot,Client,EmailSubscriber,PDFFile
from django.contrib.auth  import authenticate,  login, logout
from django.forms import Form, CharField, EmailField
from .forms import BookingForm, EmailSubscriptionForm
import uuid
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count

# Create your views here.
def home(request):
    blogPost = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
    techBlogPost = TechPost.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
    context = {'blogPostsByLike': blogPost, 'techBlogPostsByLike': techBlogPost}
    return render(request, 'home/home.html', context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if name is None:
            messages.error(request, "Please Enter your name")
        elif email is None:
            messages.error(request, "Please enter your Email")
        elif len(phone)<10 or phone is None:
            messages.error(request, "Please Enter you contact detail correctly with country code")
        elif phone[0] !='+':
            messages.error(request, "Please Enter country code with + in beginning")    
        elif content is None:
            messages.error(request, "Please Enter content of your query/message")    
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def about(request): 
    return render(request, 'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>80 or len(query)==0:
        allPosts=Post.objects.none()
        allTechPosts=TechPost.objects.none()
    else:
        #For Blog App
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
        #For Tech Blog App
        allTechPostsTitle= TechPost.objects.filter(title__icontains=query)
        allTechPostsAuthor= TechPost.objects.filter(author__icontains=query)
        allTechPostsContent =TechPost.objects.filter(content__icontains=query)
        allTechPosts=  allTechPostsTitle.union(allTechPostsContent, allTechPostsAuthor)

    if allPosts.count() ==0 and allTechPosts.count()==0:
        if len(query)>80:
            messages.warning(request, "No search results found. Please refine your query.")
        elif len(query)==0:
            messages.warning(request, "Search text is empty, Please enter a query in search text field")    
    params={'allPosts': allPosts, 'allTechPosts':allTechPosts, 'query': query}
    return render(request, 'home/search.html', params)
#change
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if User.objects.filter(username__icontains=username):
            messages.error(request, "This username can not be taken as it already")
        if len(username)>30:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, f" Your account has been successfully created with username {username}")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")    

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")
    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
'''heheeh'''
def available_slots(request):
    slots = Slot.objects.filter(is_available=True)
    return render(request, 'home/available_slots.html', {'slots': slots})

def generate_session_id():
    session_id = str(uuid.uuid4())
    return session_id

def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, pk=slot_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            slot.is_available = False
            slot.name = form.cleaned_data['name']
            slot.email = form.cleaned_data['email']
            slot.phone_number = form.cleaned_data['phone_number']
            slot.country_code = form.cleaned_data['country_code']

            session_id = generate_session_id()
            myclient=Client(name=slot.name,email=slot.email,phone_number=slot.phone_number,
                            country_code=slot.country_code,unique_session_id=session_id)
            slot.session_id = session_id
            slot.save()
            myclient.save()
            messages.success(request, f"A session has been booked with unique reference ID: {session_id}")
            return redirect('/')
    else:
        form = BookingForm()

    return render(request, 'home/book_slot.html', {'slot': slot, 'form': form})



def booking_success(request):
    return render(request, 'home/booking_success.html')



def PDF(request):
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber = EmailSubscriber.objects.create(email=email)
            pdf_file = get_object_or_404(PDFFile, id=1)
            # Generate the download link
            download_link = f"http://{get_current_site(request).domain}/download_pdf/{pdf_file.id}/"

            # Send the verification email with download link
            subject = 'Email Subscription Confirmation'
            html_message = render_to_string('home/verification_email.html', {
                'subscriber': subscriber,
                'download_link': download_link,
            })

            # Create the EmailMultiAlternatives object
            email_message = EmailMultiAlternatives(subject, html_message, 'goodhomelander@gmail.com', [email])
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()

            messages.success(request, "An email has been sent to your provided email ID, Kindly click on Download button to download the PDF.")
            return redirect(f"/after_email_subs")
    else:
        form = EmailSubscriptionForm()

    return render(request, 'home/subscribe.html', {'form': form})


def download_pdf(request, pdf_id):
    try:
        pdf_file = PDFFile.objects.get(pk=pdf_id)
    except PDFFile.DoesNotExist:
        return HttpResponse("PDF file not found.", status=404)

    response = HttpResponse(pdf_file.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf_file.file}"'
    return response


def after_email_subs(request):
    return redirect(f"/")


