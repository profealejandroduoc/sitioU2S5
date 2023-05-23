from django.contrib import admin
from .models import Persona, Mascota

# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre", "apellido", "edad", "sexo"]
    list_editable=["nombre", "apellido", "edad", "sexo"]
    list_filter=["nombre", "apellido","edad"]

    class meta:
        model=Persona

class admMascota(admin.ModelAdmin):
    list_display=["id","tipo","nombre","propietario"]
    lista_editable=["tipo","nombre","propietario"]

    class meta:
        model=Mascota

admin.site.register(Persona,admPersona)
admin.site.register(Mascota,admMascota)