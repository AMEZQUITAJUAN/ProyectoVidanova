from django.urls import path
from . import views

urlpatterns = [
    path('', views.indicators, name='indicators'),
    ]