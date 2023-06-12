from django.db import models
from LIBRARY.models import Lecteur, livre

class Emprunt(models.Model):
    
    Lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
    livre = models.ForeignKey(livre, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField()
    Date_retour = models.DateTimeField()