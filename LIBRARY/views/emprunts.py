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