from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from LIBRARY.models import Emprunt
from LIBRARY.Forms import EmpruntForm,emprunt_form
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
    if request.method =="POST":
        empruntForm = EmpruntForm(request.POST)
        if empruntForm.is_valid():
            post = empruntForm.save()
            messages.success(request,"Le livre a ete bien enregistre avec succes")
            return redirect('home')
        else:
            return render (request,'app/emprunts/ajout_emprunt.html',{'empruntForm':empruntForm})    
    elif request.method =="GET" :
        empruntForm = EmpruntForm()
        context = {'emprentForm':empruntForm}
        return render (request, 'app/emprunts/ajout_emprunt.html',context)

    
  