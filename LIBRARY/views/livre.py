
from django.shortcuts import redirect,render
from models.livre import livre
from LIBRARY.forms import LivreForm

def ajout_livre(request):
    if request.method=="POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/afficher_livre")
            except:
                pass
    else:
        form = LivreForm()
    return render(request,'ajouter_livre.html',{'form':form})

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
