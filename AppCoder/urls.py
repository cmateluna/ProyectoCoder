from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name="coder-inicio"), #esta era nuestra primera pagina
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("estudiantes/crear/", creacion_estudiantes, name="coder-estudiantes-crear"),
    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/crear/", creacion_profesores, name="coder-profesores-crear"),
    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/crear/", creacion_curso, name="coder-cursos-crear"),
    path("cursos/borrar/<id>/", eliminar_curso, name="coder-cursos-borrar"),
    path("cursos/actualizar/<id>/", editar_curso, name="coder-cursos-editar"),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultados/", resultados_busqueda_cursos, name="coder-cursos-buscar-resultados"),
    path("entregables/", entregables, name="coder-entregables"),
    path("test/", test),
]
