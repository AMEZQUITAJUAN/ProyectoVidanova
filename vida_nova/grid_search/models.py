from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    age=models.IntegerField()
    nid=models.CharField(max_length=10)

    def __str__(self):
        return self.name

# class MedicalRequest(models.Model):
#     # Referencia al modelo Patient que está en la app indicadores
#     patient = models.ForeignKey(
#         'indicadores.Patient',
#         on_delete=models.CASCADE,
#         related_name='medical_requests'
#     )

# class Meta:
#     verbose_name = "Medical Request"
#     verbose_name_plural = "Medical Requests"

#     def __str__(self):
#         return f"Request {self.id} - {self.patient.full_name}"
