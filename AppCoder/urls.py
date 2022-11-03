from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("cursos/", cursos),
    path("entregables/", entregables),
]
