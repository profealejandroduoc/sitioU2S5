#URLS.py aplicacion
from django.contrib import admin
from django.urls import path
from .views import index, paginita

urlpatterns=[
    path('',index,name="index"),
    path('paginita',paginita,name="paginita")
]