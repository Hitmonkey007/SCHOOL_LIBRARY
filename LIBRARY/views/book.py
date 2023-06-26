from django.shortcuts import redirect,render
from LIBRARY.models import livre
from LIBRARY.Forms import LivreForm


from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from LIBRARY.models import *
from LIBRARY.Forms import *


def ajouter(request):
    if request.method=="POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/afficher")
            except:
                pass
    else:
        form = LivreForm()
    return render(request,'livres/ajouter.html',{'form':form})

def afficher(request):
    livres = livre.objects.all()
    return render(request,'afficher.html',{'livres':livres})

def modifier(request,id):
    livres = livre.objects.get(id=id)
    return render(request,'modifier.html',{'livres':livres})

def update(request,id):
    livres = livre.objects.get(id=id)
    form = LivreForm(request.POST,instance=livres)
    if form.is_valid():
        form.save()
        return redirect("/afficher")   
    return render(request,'modifier.html',{'livres':livres})

def supprimer(request,id):
    livres = livre.objects.get(id=id)
    livres.delete()
    return redirect("/afficher")

