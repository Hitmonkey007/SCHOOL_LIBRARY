
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from LIBRARY.models import *
from LIBRARY.Forms import *


def ajouter_livre(request):
    if request.method== "POST" :
        form = LivreForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home') 
        else :
            return render(request, 'app/livres/ajouter_livre.html', {'form': form}) 
        
    elif request.method == "GET": 
        form = LivreForm()
        context = {'form': form }
        return render(request, 'app/livres/ajouter_livre.html', context)
        
              
        
        """
        if form.is_valid():
            try:
                form.save()
                return redirect("/afficher_livre")
            except:
                pass
    else:
        form = LivreForm()
    return render(request,'ajouter_livre.html',{'form':form})
"""
def affiche_livre(request):
    livres = livre.objects.all()
    return render(request,'show.html',{'livres':livres})

def modifier_livre(request,id):
    livres = livre.objects.get(id=id)
    return render(request,'modifier_livre.html',{'livres':livres})

def update(request,id):
    livres = livre.objects.get(id=id)
    form = LivreForm(request.POST,instance=livres)
    if form.is_valid():
        form.save()
        return redirect("/afficher_livre")   
    return render(request,'modifier_livre.html',{'livres':livres})

def supprimer_livre(request,id):
    livres = livre.objects.get(id=id)
    livres.delete()
    return redirect("/afficher_livre")


def index(request):
     livreForm = Livre.objects.all()
     return render(
        request,
        'app/livres/index.html',
        {
            'livreForm': livreForm
        }
    )

