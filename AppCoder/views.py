from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Curso, Profesor

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


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")

def creacion_profesores(request):
    
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data      
            
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])

            profesor.save() 
            
        return render(request, "AppCoder/index.html")    
    
    else:
        formulario = ProfesorFormulario()
        
    contexto = {"formulario": formulario}         
    return render(request, "AppCoder/profesores_formularios.html", contexto)

def buscar_curso(request):
    
    return render(request, "AppCoder/busqueda_cursos.html")


def resultados_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]
    
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "AppCoder/resultados_busquedas_cursos.html", {"cursos": cursos})


def entregables(request):
    return render(request, "AppCoder/entregables.html")

