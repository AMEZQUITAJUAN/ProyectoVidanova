# from django.contrib import admin
# from .models import MedicalRequest
# #, Patient

# @admin.register(MedicalRequest)
# class MedicalRequestAdmin(admin.ModelAdmin):
#     list_display = (
#         "case_type", "intake_date", "procedure_type", "request_status",
#         "request_date", "appointment_date", "provider", "care_pathway", "month", "patient"
#     )
#     search_fields = ("case_type", "provider", "patient__first_name", "patient__last_name")
#     list_filter = ("case_type", "request_status", "care_pathway", "month")

# # @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name", "identification", "birth_date", "city", "phone", "email")
#     search_fields = ("first_name", "last_name", "identification", "city")
#     list_filter = ("city",)
    