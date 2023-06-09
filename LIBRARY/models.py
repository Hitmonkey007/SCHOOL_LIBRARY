from django.db import models

# Create your models here.
class livre(models.livre):
    id_livre = models.CharField(max_length=30)
    id_auteur = models.CharField(max_length=30)
    titre = models.CharField(max_length=100)
    exemplaire = models.IntegerField
    annee_publication = models.DateField
