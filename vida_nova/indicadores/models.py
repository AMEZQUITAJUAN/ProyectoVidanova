from django.db import models

class board(models.Model):
    name = models.CharField(max_length=100)
    stage= models.CharField(max_length=100)# consulta, examenes, biopsia, tratamiento, seguimiento
    start_date = models.DateField()
    days_left = models.IntegerField()# cuatos dias quedan para el vencimiento de tarea
    alert = models.BooleanField() # si los dias son menos de rojo si faltan <3 días, amarillo si <7, verde si >7)
    # Completar de acuerdo a modelo ER
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Completar de acuerdo a modelo ER