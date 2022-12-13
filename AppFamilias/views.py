from django.shortcuts import render
from .models import Familiar1,Familiar2,Familiar3
from django.http import HttpResponse

# Create your views here.

def familiar1(request):
    familiar1=Familiar1(nombre_apellido="Juan Perez",nacimiento=1998,dni=40256974)
    familiar1.save()
    cadena_texto1=f"familiar guardado: Nombre: {familiar1.nombre_apellido}, Nacimiento: {familiar1.nacimiento}, DNI: {familiar1.dni}"
    return HttpResponse(cadena_texto1)


def familiar2(request):
    familiar2=Familiar2(nombre_apellido="Laura Fernandez",nacimiento=2004,dni=45589417)
    familiar2.save()
    cadena_texto2=f"familiar guardado: Nombre: {familiar2.nombre_apellido}, Nacimiento: {familiar2.nacimiento}, DNI: {familiar2.dni}"
    return HttpResponse(cadena_texto2)


def familiar3(request):
    familiar3=Familiar3(nombre_apellido="Martina Sanchez",nacimiento=1958,dni=13472684)
    familiar3.save()
    cadena_texto3=f"familiar guardado: Nombre: {familiar3.nombre_apellido}, Nacimiento: {familiar3.nacimiento}, DNI: {familiar3.dni}"
    return HttpResponse(cadena_texto3)

