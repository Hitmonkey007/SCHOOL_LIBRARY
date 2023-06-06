from django.shortcuts import render
from django.http import HttpRequest


def index(request):
    return render(
        request,
        'app/home/index.html'
    )
    
    
def contact(request):
    return render(
        request,
        'app/home/contact.html'
    )

