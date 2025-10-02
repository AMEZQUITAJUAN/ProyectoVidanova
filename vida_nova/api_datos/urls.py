from django.urls import path
from .views import PacienteListView, consumir_api 

urlpatterns = [
    path('', PacienteListView.as_view(), name='paciente-list'),   
    path('pacientes/', consumir_api, name='consumir-api'),        
]