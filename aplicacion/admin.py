from django.contrib import admin
from .models import Persona, Mascota, Producto

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

class admProducto(admin.ModelAdmin):
    list_display=["id","descripcion","precio"]
    list_editable=["descripcion","precio"]

    class meta:
        model=Producto

admin.site.register(Persona,admPersona)
admin.site.register(Mascota,admMascota)
admin.site.register(Producto,admProducto)