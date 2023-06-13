from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from LIBRARY.models import Emprunt
from LIBRARY.Forms import EmpruntForm



def index(request):
    assert isinstance(request, HttpRequest)
    orders = Emprunt.objects.all()
    return render(
        request,
        'app/emprunts/index.html',
        {
            'emprunts': Emprunt
        }
    )
