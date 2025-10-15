from django.urls import path
from . import views

urlpatterns = [
    # Cursos
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),

    # Alumnos
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('alumnos/editar/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('alumnos/eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
]
