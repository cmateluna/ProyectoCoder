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
    return render(request, "AppCoder/cursos.html")

def creacion_curso(request):
    
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]
        
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
    
    return render(request, "AppCoder/curso_formulario.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

