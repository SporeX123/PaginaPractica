from django.shortcuts import render
from django.urls import path
from . import views
from django.http import HttpResponse

def index(request):
    """
    Vista principal de la pagina de inicio.
    Recibe una peticion HTTP y devuelve una respuesta simple.
    """
    return HttpResponse("Hola que tal, soy colosal")

# Create your views here.

