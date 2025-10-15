from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Alumno
from .forms import CursoForm, AlumnoForm

# --- CURSOS ---
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/form.html', {'form': form})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/form.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('lista_cursos')


# --- ALUMNOS ---
def lista_alumnos(request):
    alumnos = Alumno.objects.select_related('curso').all()
    return render(request, 'alumnos/lista.html', {'alumnos': alumnos})

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/form.html', {'form': form})

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/form.html', {'form': form})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    alumno.delete()
    return redirect('lista_alumnos')
