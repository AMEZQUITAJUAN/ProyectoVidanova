from django.db import models

class MedicalRequest(models.Model):
    # Referencia al modelo Patient que está en la app indicadores
    patient = models.ForeignKey(
        'indicadores.Patient',
        on_delete=models.CASCADE,
        related_name='medical_requests'
    )
    request_date = models.DateField()
    request_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Medical Request"
        verbose_name_plural = "Medical Requests"

    def __str__(self):
        return f"Request {self.id} - {self.patient.full_name}"
