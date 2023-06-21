from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect



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
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
         login(request, user)
        
        return render(request, 'app/home/index.html' )
     
         
    return render(request, "app/home/signin.html")


