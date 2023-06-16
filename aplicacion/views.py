from django.shortcuts import get_object_or_404, render,redirect
from datetime import date
from .models import Persona,Mascota,Usuario
from .forms import formCrearMascota, formCrearPersona, formEditarPersona ,frmCrearUsuario, frmUsuarioExtendido
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

def index(request):
   
    return render(request,'aplicacion/index.html')

def crearcuentaextendida(request):
    formext=frmUsuarioExtendido()
    formnormal=frmCrearUsuario()
    contexto={
        "formext":formext,
        "formnormal":formnormal
    }

    if request.method=="POST":
        formnormal=frmCrearUsuario(data=request.POST)
        formext=frmUsuarioExtendido(data=request.POST)
        if formnormal.is_valid() and formext.is_valid():
            #GUARDAR USUARIO DE DJANGO AUTH
            formnormal.save() #usuario django creado
            datos_usr_django=formnormal.cleaned_data

            #BUSCAR USUARIO CREADO EN TABLA DE DJANGO
            usrdj=User.objects.get(username=datos_usr_django.get("username"))
            #crear un objeto usuario con mi modelo
            usr=Usuario()
            #pasar lo datos del formulario a mi usuario personalizado
            datos_ext=formext.cleaned_data
            usr.rut=datos_ext.get("rut")
            usr.direccion=datos_ext.get("direccion")
            usr.usrdjango=usrdj
            #guadar mi usuario en la tabla de mi aplicacion
            usr.save()
            return redirect(to="index")           
            
        
    return render(request,"registration/cuentaextendida.html",contexto)

def crearcuenta(request):
    form=frmCrearUsuario()
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmCrearUsuario(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="index")
        
    return render(request,"registration/crearcuenta.html",contexto)

@permission_required('aplicacion.view_persona')
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

@permission_required('aplicacion.add_persona')
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

def eliminarpersona(request, id):
    kill=Persona.objects.get(rut=id)

    try:
        pet=Mascota.objects.filter(propietario_id=kill.rut)
       
        
    except:
        print("***************ERROR***********************")
        pet=None 
   
    contexto={
        "persona":kill,
        "pet":pet
    }
    if request.method=="POST":
        kill=Persona.objects.get(rut=id)
        
        kill.delete()
        return redirect(to="personas")      

    return render(request,"aplicacion/personas/delete.html",contexto)

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