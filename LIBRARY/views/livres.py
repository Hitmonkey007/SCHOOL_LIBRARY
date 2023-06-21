
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from LIBRARY.models import *
from LIBRARY.Forms import *






def add(request):
    form = LivreForm()
    return render(
        request,
        'app/livres/add.html',
        {
            'form' : form
        }
    )
      
def livres_Form(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le Livre est enregistré Avec Succès !")
    #retour a la page
    return redirect('/livres')

def index(request):
     livreForm = livre.objects.all()
     return render(
        request,
        'app/livres/index.html',
        {
            'livreForm': livreForm
        }
    )
