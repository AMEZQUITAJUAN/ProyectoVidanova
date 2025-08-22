from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminboard, name='adminboard'),
    ]