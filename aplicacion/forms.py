from django import forms
from .models import Mascota, Persona

class formCrearPersona(forms.ModelForm):
    
    class Meta:
        model=Persona
        fields=["rut","nombre", "apellido", "edad", "sexo"]

class formEditarPersona(forms.ModelForm):
    
    class Meta:
        model=Persona
        fields=["nombre", "apellido", "edad", "sexo"]


class formCrearMascota(forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = ["id","tipo","nombre","propietario"]
