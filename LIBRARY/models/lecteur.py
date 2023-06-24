"""pour les lecteurs"""

from django.db import models 


class Lecteur(models.Model):
    catchoice= [
        ('homme', 'Homme'),
        ('femme', 'Femme')
        ]
    nom= models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    Adresse = models.CharField(max_length=40)
    categorie=models.CharField(max_length=30,choices=catchoice,default='homme')
    telephone=models.CharField(max_length=10)
    #utiliser pour donner un livre
    def __str__(self):
        return str (self.nom)+'['+str(self.prenom)+']'