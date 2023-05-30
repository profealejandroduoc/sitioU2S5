from django import forms
from .models import Persona

class formCrearPersona(forms.ModelForm):
    
    class Meta:
        model=Persona
        fields=["rut","nombre", "apellido", "edad", "sexo"]
