from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('asistencial', 'Asistencial'),
        ('callcenter', 'Call Center'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Rol")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']
