from django.shortcuts import render
from .models import Genero,Alumno
# Create your views here.


def index(request):

    alumnos = Alumno.objects.all()
    context = {"Alumnos":alumnos}
    return render(request, "alumnos/index.html", context)


def listadoSQL(request):
    alumnos = Alumno.objets.raw("SELECT * FRM alumnos_alumno")
    context = {"alumnos":alumnos}
    return render(request, "alumnos/listadoSQL.html", context)