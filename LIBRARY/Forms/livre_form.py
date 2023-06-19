from django.forms import ModelForm
from LIBRARY.models import livre

class LivreForm(ModelForm):
    
    class Meta:
        model = livre
        fields = '__all__'