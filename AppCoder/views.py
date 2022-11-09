from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

# def curso(self):

#     curso = Curso(nombre="Desarrollo web", camada="19881")
#     curso.save()
#     documentoDeTexto = f"----->Curso: {curso.nombre}  Camada: {curso.camada}"

#     return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/base.html")

def cursos(request):
    # Obtener el listado de objecto en la BD
    cursos = Curso.objects.all()
    
    for curso in cursos:
        print(curso.nombre)
    
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

