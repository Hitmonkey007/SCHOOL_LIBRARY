from django.shortcuts import render
from django.http import HttpRequest


def index(request):
    return render(
        request,
        'app/home/index.html'
    )
 
def signup(request):
    pass   

def signin(request):
    pass
    
def contact(request):
    return render(
        request,
        'app/home/contact.html'
    )