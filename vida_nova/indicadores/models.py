from django.db import models
from django.utils import timezone

class Board(models.Model):
    name = models.CharField(max_length=100)
    stage= models.CharField(max_length=100)# consulta, examenes, biopsia, tratamiento, seguimiento
    start_date = models.DateField()
    days_left = models.IntegerField()     # cuatos dias quedan para el vencimiento de tarea
    alert = models.BooleanField()   # si los dias son menos de rojo si faltan <3 días, amarillo si <7, verde si >7)
                               # Completar de acuerdo a modelo ER
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    id_type = models.CharField(max_length=50)  # Tipo de Identificación
    phone_numbers = models.CharField(max_length=100)
    emails = models.CharField(max_length=150)
    gender = models.CharField(max_length=20)
    occupation = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    socioeconomic_status = models.CharField(max_length=20)  # Estrato
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  # Departamento
    city_of_residence = models.CharField(max_length=100)
    age = models.IntegerField()
    vital_status = models.CharField(max_length=10)

class MedicalRequest(models.Model):
    case_type = models.CharField(max_length=100,blank=True, null=True)                # Tipo de Caso
    intake_date = models.DateField(blank=True, null=True)                            # Fecha de captación
    procedure_type = models.CharField(max_length=100,blank=True, null=True)           # Tipo de procedimiento
    request_status = models.CharField(max_length=100,blank=True, null=True)           # Estado de la solicitud
    request_date = models.DateField(blank=True, null=True)      # Fecha de solicitud
    appointment_date = models.DateField(default=timezone.now)                       # Fecha de cita
    provider = models.CharField(max_length=150,blank=True, null=True)                 # Prestador
    barrier = models.TextField(blank=True, null=True)           # Barrera (zona rural, transporte, etc.)
    observations = models.TextField(blank=True, null=True)      # Observaciones
    timeliness = models.IntegerField(blank=True, null=True)     # Oportunidad (días entre solicitud y cita, por ejemplo)
    care_pathway = models.CharField(max_length=100, blank=True, null=True)             # Ruta
    month = models.CharField(max_length=20, blank=True, null=True)                     # Mes
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.case_type} - {self.intake_date}"