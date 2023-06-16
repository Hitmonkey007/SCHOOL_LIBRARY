from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages

from LIBRARY.models import Lecteur
from LIBRARY.Forms import LecteurForm

def add(request):
    return render(
        request,
        'app/lecteurs/Add.html'
    )    

def index(request):
     assert isinstance(request, HttpRequest)
     orders = Lecteur.objects.all()
     return render(
        request,
        'app/lecteurs/index.html',
        {
            'lecteurs': Lecteur
        }
    )

def edit(request):
    assert isinstance(request, HttpRequest)
    orders = Lecteur.objects.all()
    return render(
        request,
        'app/lecteurs/edit.html'
    )        

def delete(request, id):
    lecteur= Lecteur.objects.get(pk=id)
    lecteur.delete()
    return redirect('/lecteurs')

def update(request, id):
    if request.method == 'POST':
        if id == 0 :
            form = LecteurForm(request.POST)
        else :
            lecteur = Lecteur.objects.get(pk=id) 
            form = LecteurForm(request.POST,instance=lecteur)
        if form.is_valid() :
            form.save()
    return redirect('/lecteurs')        
