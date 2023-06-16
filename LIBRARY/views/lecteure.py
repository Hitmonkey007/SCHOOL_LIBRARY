from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages

from LIBRARY.models import Lecteur
from LIBRARY.Forms import LecteurForm

def add(request):
  if request.method == "POST":
       lecteurForm = LecteurForm(request.POST)

       if lecteurForm.is_valid():
          post = lecteurForm.save(commit=False)
          post.save()
          messages.success(request, "Le lecteur a ete enregistre avec succes")
          return redirect('home')
       else:
      
          return render(request, 'app/lecteurs/add.html', {'lecteurForm': lecteurForm})

  elif request.method == "GET":
       lecteurForm = LecteurForm()
       context = {'lecteurForm': lecteurForm}
       return render(request, 'app/lecteurs/Add.html', context)
       
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
