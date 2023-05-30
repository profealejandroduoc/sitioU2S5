from django.shortcuts import render,redirect
from datetime import date
from .models import Persona,Mascota
from .forms import formCrearPersona 

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

def crearpersona(request):
    form=formCrearPersona(request.POST or None)
   
    contexto={
        "formulario":form,
        
    }

    if form.is_valid():
        instanciaPersona=form.save(commit=False)
        instanciaPersona.save()
        return redirect(to="personas")
     
       
    

    return render(request,"aplicacion/crearpersona.html",contexto)
