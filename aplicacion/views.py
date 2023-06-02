from django.shortcuts import get_object_or_404, render,redirect
from datetime import date
from .models import Persona,Mascota
from .forms import formCrearMascota, formCrearPersona, formEditarPersona 

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
    return render(request,'aplicacion/personas/personas.html',contexto)

def crearpersona(request):
    form=formCrearPersona(request.POST or None)
   
    contexto={
        "formulario":form,
        
    }

    if form.is_valid():
        instanciaPersona=form.save(commit=False)
        instanciaPersona.save()
        return redirect(to="personas")
     
       
    

    return render(request,"aplicacion/personas/crearpersona.html",contexto)

def editarpersona(request,id):
    persona=get_object_or_404(Persona,rut=id)

    form=formEditarPersona(instance=persona)


    contexto={
        "persona":persona,
        "form":form
    }

    if request.method=="POST":
        form=formEditarPersona(data=request.POST,instance=persona)

    if form.is_valid():
        modpersona=Persona.objects.get(rut=persona.rut)
        datos=form.cleaned_data

        modpersona.nombre=datos.get("nombre")
        modpersona.apellido=datos.get("apellido")
        modpersona.edad=int(datos.get("edad"))
        modpersona.sexo=datos.get("sexo")
        modpersona.save()
        return redirect(to="personas")

    return render(request,"aplicacion/personas/editar.html",contexto)


def mascotas(request):
    pets=Mascota.objects.all()

    contexto={
        "pets":pets
    }


    return render(request,"aplicacion/mascotas/mascotas.html",contexto)


def crearmascota(request):
    formulario=formCrearMascota(request.POST or None)

    contexto={
        "form":formulario
    }

    if formulario.is_valid():
        mascota=formulario.save(commit=False)
        mascota.save()
        return redirect(to="mascotas")

    return render(request,"aplicacion/mascotas/crear.html",contexto)