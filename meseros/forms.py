from django import forms
from .models import Meseros

class MeseroForm(forms.ModelForm):
    class Meta:
        model = Meseros
        fields = ['nombre', 'edad', 'nacionalidad', 'dni']
