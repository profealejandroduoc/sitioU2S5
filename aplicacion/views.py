from django.shortcuts import render
from datetime import date
from .models import Persona,Mascota

def index(request):
    return render(request,'aplicacion/index.html')

def personas(request):
    fecha=date.today()
    autor="El profe"
    people=Persona.objects.all()

    contexto={
        "fecha":fecha,
        "autor":autor,
        "personas":people
    }
    return render(request,'aplicacion/personas.html',contexto)
