from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request,"aplicacion/index.html")


def paginita(request):
    fecha=date.today()
    
    context={
        "date":fecha
    }

    return render(request,"aplicacion/paginita.html",context)