from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='cursos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumnos')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='alumnos/')
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"