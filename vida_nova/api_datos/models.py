from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=250)
    procedmiento = models.TextField()
    
    def __str__(self):
        return self.nombre
    

