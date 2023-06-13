from django.shortcuts import render
from django.http import HttpRequest

def ajout_lecteur(request):
    return render(
        request,
        'app/home/Ajout_lecteur.html'
    )    

def lecteurs(request):
    return render(
        request,
        'app/home/lecteurs.html'
    )    