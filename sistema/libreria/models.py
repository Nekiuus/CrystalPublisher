from django.db import models

# models.py
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True)

def __str__(self):
    
    return self.titulo


