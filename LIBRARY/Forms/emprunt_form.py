from django.forms import ModelForm
from LIBRARY.models import Emprunt

class EmpruntForm(ModelForm):
    
    class Meta:
        model = Emprunt
        fields = '__all__'