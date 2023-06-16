from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):
    return render(
        request,
        'app/home/index.html'
    )
 
def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render( request, 'signin.html')
    
def contact(request):
    return render(
        request,
        'app/home/contact.html'
    )