from django.forms import ModelForm
from .models import Fillup  

class FillupForm(ModelForm):
    class Meta:
        model = Fillup
        fields = ['date', 'gas_station', 'cost']