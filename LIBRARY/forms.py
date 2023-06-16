from django import forms
from django.forms import fields
from models.livre import livre

class LivreForm(forms.ModelForm): 
    class Meta:
        model = livre
        fields = "__all__"