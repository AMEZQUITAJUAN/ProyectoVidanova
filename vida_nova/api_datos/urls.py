from django.urls import path
from .views import PacienteListView, consumir_api  # importa la vista consumir_api también

urlpatterns = [
    path('', PacienteListView.as_view(), name='paciente-list'),   # Ruta API REST
    path('pacientes/', consumir_api, name='consumir-api'),        # Ruta para mostrar la plantilla HTML
]
