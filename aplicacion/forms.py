from django import forms
from .models import Mascota, Persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class frmCrearUsuario(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1",'password2']

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
