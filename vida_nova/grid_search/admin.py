from django.contrib import admin

from .models import Patient, MedicalRequest, Data

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "identification")
    search_fields = ("first_name", "last_name", "identification")

@admin.register(MedicalRequest)
class MedicalRequestAdmin(admin.ModelAdmin):
    list_display = ("case_type", "request_date", "patient")

admin.site.register(Data)
