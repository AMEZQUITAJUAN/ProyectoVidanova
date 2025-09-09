from django.urls import path
from .views import pacientelistView

urlpatterns = [
    path('', pacientelistView.as_view(), name='paciente-list'),
    ]