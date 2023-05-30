#URLS.py aplicacion
from django.contrib import admin
from django.urls import path
from .views import index,personas, crearpersona

urlpatterns=[
    path('',index,name="index"),
    path('personas',personas,name="personas"),
    path('crearpersona',crearpersona,name="crearpersona")

]