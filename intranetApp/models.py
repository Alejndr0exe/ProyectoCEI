from django.db import models

# Create your models here.
class Script (models.Model):
    documento = models.FileField(upload_to='script/', unique=True )
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def delete(self):
        self.documento.delete()
        super().delete()

class Data (models.Model):
    documento = models.FileField(upload_to='data/', unique=True)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def delete(self):
        self.documento.delete()
        super().delete()


class Manual (models.Model):
    documento = models.FileField(upload_to='manual/', unique=True)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def delete(self):
        self.documento.delete()
        super().delete()



