from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from LIBRARY.models import *
from LIBRARY.Forms import *


def add(request):
    if request.method == "POST":
         livreForm =LivreForm(request.POST)
         if livreForm.is_valid():
              post =livreForm.save()
              messages.success(request, "Le livre a ete enregistre avec succes")
              return redirect('/add')
         else:
              return render(request, 'app/livres/add.html', {'livreForm':livreForm})

    elif request.method == "GET":
        
         livreForm =LivreForm()
         context = {'livreForm':livreForm}
         return render(request, 'app/livres/add.html', context)
  
def index(request):
     livreForm = livre.objects.all()
     return render(
        request,
        'app/livres/index.html',
        {
            'livreForm': livreForm
        }
    )   
     

def delete(request, id):
    lecteur= Lecteur.objects.get(pk=id)
    lecteur.delete()
    return redirect('/livres/')

   