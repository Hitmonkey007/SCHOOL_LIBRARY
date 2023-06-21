from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from LIBRARY.models import *
from LIBRARY.Forms import *

def add(request):

  if request.method == "POST":
       lecteurForm = LecteurForm(request.POST)

       if lecteurForm.is_valid():
          post = lecteurForm.save()
          messages.success(request, "Le lecteur a ete enregistre avec succes")
          return redirect('/lecteurs')
       else:
      
          return render(request, 'app/lecteurs/add.html', {'lecteurForm': lecteurForm})

  elif request.method == "GET":
       lecteurForm = LecteurForm()
       context = {'lecteurForm': lecteurForm}
       return render(request, 'app/lecteurs/Add.html', context)
       
def index(request):
     lecteurForm = Lecteur.objects.all()
     return render(
        request,
        'app/lecteurs/index.html',
        {
            'lecteurForm': lecteurForm
        }
    )

def edit(request,id):
    assert isinstance(request, HttpRequest)
    lecteur = Lecteur.objects.get(pk=id)
    return render(
        request,
        'app/lecteurs/edit.html'
    )        

def delete(request, id):
    lecteur= Lecteur.objects.get(pk=id)
    lecteur.delete()
    return redirect('/lecteurs/')

def update(request, id):
   lecteur = Lecteur.objects.get(pk=id)
   lecteurForm = LecteurForm(request.POST or None, instance= lecteur)
   if lecteurForm.is_valid():
      lecteurForm.save()
      return redirect('lecteur_index')

   return render  (
       request,
       'app/lecteurs/edit.html'
       )   