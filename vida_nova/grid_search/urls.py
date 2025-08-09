from django.urls import path
from . import views

urlpatterns = [
    path('', views.grid_view, name='grid_view'),
    ]