#URLS.py aplicacion
from django.contrib import admin
from django.urls import path
from .views import crearcuenta, editarpersona, index,personas, crearpersona,mascotas,crearmascota, eliminarpersona, crearcuentaextendida

urlpatterns=[
    path('',index,name="index"),
    path('personas',personas,name="personas"),
    path('crearpersona',crearpersona,name="crearpersona"),
    path('mascotas',mascotas,name="mascotas"),
    path('crearmascota',crearmascota,name="crearmascota"),
    path('editarpersona/<id>',editarpersona,name="editarpersona"),
    path('eliminarpersona/<id>',eliminarpersona,name="eliminarpersona"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('crearcuentaextendida',crearcuentaextendida,name="crearcuentaextendida")

]