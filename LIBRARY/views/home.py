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
    
    return render(request, 'app/home/signup.html')

def signin(request):
    return render( request, 'app/home/signin.html')
    
def contact(request):
    return render(
        request,
        'app/home/contact.html'
    )