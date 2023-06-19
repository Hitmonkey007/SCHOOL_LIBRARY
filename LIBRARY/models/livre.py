"""pour les livres modeling"""
from django.db import models
class livre(models.Model):
    catchchoice = [
        ('histoire','histoire'),
        ('geographie','geographie'),
        ('histoire & geographie','histoire & geographie'),
        ('informatique','informatique'),
        ('busness','busness')
    ]
    id_livre = models.CharField(max_length=30)
    id_auteur = models.CharField(max_length=30)
    titre = models.CharField(max_length=100)
    exemplaire = models.IntegerField()
    annee_publication = models.DateField()
    categorie = models.CharField(max_length=100,choices=catchchoice,default='histoire')
    

    