from django.db import models

# Create your models here.
class News(models.Model):
    encabezado = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length = 255)
    fecha = models.DateField()
    cuerpo = models.TextField()
