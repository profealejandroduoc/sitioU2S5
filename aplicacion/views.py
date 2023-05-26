from django.shortcuts import render
from datetime import date

def index(request):
    return render(request,'aplicacion/index.html')
