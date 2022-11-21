from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.forms import ProfesorFormulario, EstudianteFormulario, CursoFormulario
from AppCoder.models import Curso, Profesor, Estudiante, Entregable


# Dependencias para resolver apertura de archivos usando rutas relativas
from ProyectoCoder.settings import BASE_DIR
import os

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def inicio(request):
    return render(request, "AppCoder/base.html")

def cursos(request):   
    
    errores = ""
    
    # Validamos tipo de peticion
    if request.method == "POST":
        
        # Cargamos los datos en el formlario
        formulario = CursoFormulario(request.POST)
        
        # Validamos los datos
        if formulario.is_valid():
            # Recuperamos los datos sanitizados
            data = formulario.cleaned_data
            # Creamos el curso
            curso = Curso(nombre=data["nombre"], camada=data["camada"])
            # Guardamos el curso
            curso.save()
        else:
            # Si el formulario no es valido guardamos los errores para mostrarlos
            errores = formulario.errors    
    
    # Recuperar todos los cursos de la BD
    cursos = Curso.objects.all() # Obtener TODOS los registro de ese modelo
    # Creamos el formulario vacio
    formulario = CursoFormulario()
    # Creamos el contexto
    contexto = {"listado_cursos": cursos, "formulario": formulario, "errores": errores}
    # Retornamos la respuesta
    return render(request, "AppCoder/cursos.html", contexto)


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save() 
            return redirect("coder-cursos")
        else:
            return render(request, "AppCoder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})
        
    else:
        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "AppCoder/editar_curso.html", {"formulario": formulario, "errores":""})    


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    
    return redirect("coder-cursos")



def creacion_curso(request):
    
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]
        
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
    
    return render(request, "AppCoder/curso_formulario.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def creacion_estudiantes(request):
    
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = formulario.cleaned_data
            
            estudiante = Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            estudiante.save()
       
    formulario = EstudianteFormulario()     
    return render(request, "AppCoder/estudiantes_formulario.html", {"formulario": formulario})    
            

def profesores(request):
    return render(request, "AppCoder/profesores.html")


def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"],
                                email=data["email"], profesion=data["profesion"])

            profesor.save()

    formulario = ProfesorFormulario()
    contexto = {"formulario": formulario}
    return render(request, "AppCoder/profesores_formulario.html", contexto)


def buscar_curso(request):
    
    return render(request, "AppCoder/busqueda_cursos.html")


def resultados_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]
    
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "AppCoder/resultados_busquedas_cursos.html", {"cursos": cursos})


def entregables(request):
    return render(request, "AppCoder/entregables.html")



def test(request):
    ruta = os.path.join(BASE_DIR, "AppCoder/templates/AppCoder/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)
    
    return HttpResponse(file.read())


class EntregablesList(ListView):
    
    model = Entregable
    template_name = "AppCoder/list_entregables.html"
    
class EntregableDetail(DetailView):
    
    model: Entregable
    template_name = "AppCoder/detail_entregable.html"    
    
class EntregableCreate(CreateView):
    
    model = Entregable 
    success_url = "/coder/entregables/"   
    fields = ["nombre", "fechaDeEntrega", "entregado"]
    template_name = "AppCoder/entregable_form.html"
    
class EntregableUpdate(UpdateView):
    
    model = Entregable 
    success_url = "/coder/entregables/"   
    fields = ["fechaDeEntrega", "entregado"]    
    
class EntregableDelete(DeleteView):
    
    model = Entregable
    success_url = "/coder/entregables/"
    
    
        