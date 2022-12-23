from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.
def home(request): 
    return render(request, 'home/home.html')

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
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        if len(query)>80:
            messages.warning(request, "No search results found. Please refine your query.")
        elif len(query)==0:
            messages.warning(request, "Search text is empty, Please enter a query in search text field")    
    params={'allPosts': allPosts, 'query': query}
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
        return redirect('home')

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
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')



