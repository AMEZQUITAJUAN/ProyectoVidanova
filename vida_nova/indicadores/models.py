from django.db import models
from django.utils import timezone

class Patient(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    identification = models.CharField(max_length=50, verbose_name="Documento de identidad", unique=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Dirección")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ciudad")
    
    def __str__(self):
        # Igual que en MedicalRequest, devolvemos algo descriptivo
        return f"{self.first_name} {self.last_name} - {self.identification}"  # si los dias son menos de rojo si faltan <3 días, amarillo si <7, verde si >7)
                            
    
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
    case_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Tipo de Caso ⚙️"
    )
    intake_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de Captación 📅"
    )
    procedure_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Tipo de Procedimiento ⏳"
    )
    request_status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Estado de la Solicitud 📌"
    )
    request_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de Solicitud 📅"
    )
    appointment_date = models.DateField(
        default=timezone.now,
        verbose_name="Fecha de Cita Programada 📅"
    )
    provider = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Prestador del Servicio 🏢"
    )
    barrier = models.TextField(
        blank=True,
        null=True,
        verbose_name="Barreras Identificadas 🚧"
    )
    observations = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones Relevantes 📝"
    )
    timeliness = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Oportunidad (días) ⏱️"
    )
    care_pathway = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Ruta Asistencial 🗺️"
    )
    month = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Mes de Registro 🗓️"
    )
    patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Paciente 🧍"
    )

    def __str__(self):
        return f"{self.case_type} - {self.intake_date}"