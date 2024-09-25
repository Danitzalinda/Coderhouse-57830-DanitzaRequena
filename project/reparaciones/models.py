from django.db import models
from django.contrib.auth.models import User

class Reparacion(models.Model):
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_reparacion = models.DateField()
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.descripcion

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  

    def __str__(self):
        return self.user.username

