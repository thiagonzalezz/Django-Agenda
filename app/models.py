from django.db import models

# Create your models here.
class Agenda(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()