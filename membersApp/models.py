from django.db import models

# Create your models here.
class Members(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50, blank=True)
    academic_rank = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    g_scholar = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='members/')
    descripcion = models.TextField()
    puesto = models.CharField(max_length=50, blank=True)
    universidad = models.CharField(max_length=50, blank=True)