from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    usrdjango=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    direccion=models.CharField(max_length=250,null=False,default="calle falsa 123")





# Create your models here.
SEX = [
    ("M", "Masculino"),
    ("F", "Femenino"),
    ("O", "Otro"),
]
class Persona(models.Model):
    rut=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50,null=False)
    edad=models.IntegerField(null=False)
    sexo=models.CharField(choices=SEX,max_length=1,null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
    
class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=25)
    nombre=models.CharField(max_length=50)
    propietario=models.ForeignKey(Persona,on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nombre} ID MASCOTA: {self.id}"
    
class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion
