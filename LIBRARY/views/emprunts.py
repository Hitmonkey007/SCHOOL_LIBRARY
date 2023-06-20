from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
def index(request):
    assert isinstance(request, HttpRequest)
    emprunts = Emprunt.objects.all()
    return render(
        request,
        'app/emprunts/index.html',
        {
            'emprunts': Emprunt
        }
    )

def ajout_emprunt(request):
    
    assert isinstance(request, HttpRequest)
    emprunts = Emprunt.objects.all()
    form = EmpruntForm()
    return render(
        
        request,
        'app/emprunts/ajout_emprunt.html',
        
        {
            
            'form': form,
            
            'categories': emprunts
            
        }
    )    