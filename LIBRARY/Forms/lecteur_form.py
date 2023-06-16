from django.forms import ModelForm
from LIBRARY.models import Lecteur

class LecteurForm(ModelForm):
    
    class Meta:
        model = Lecteur
        fields = '__all__'