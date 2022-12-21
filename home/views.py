from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post
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
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)