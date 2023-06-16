from django.http import HttpRequest
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

#Views..
def index(request):
    return render(
        request,
        'app/home/index.html'
    )
 
def signup(request):
    if request.method == "POST":
    
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['Email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
       

        myuser = User.objects.create_user(uname, email, pass1)
        myuser.save()
        messages.success(request, 'Your account has been successfully created')
        return redirect('signin')
    
    
    return render(request, 'app/home/signup.html')

def signin(request):
    return render( request, 'app/home/signin.html')
    
def contact(request):
    return render(
        request,
        'app/home/contact.html'
    )