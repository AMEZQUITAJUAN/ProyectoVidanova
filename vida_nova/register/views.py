from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            Profile.objects.create(user=user, role=role)

            login(request, user)  # ← Loguea automáticamente
            messages.success(request, f"¡Bienvenido {user.first_name}! Tu cuenta fue creada exitosamente.")
            return redirect('home')  # Cambia por la vista de inicio o dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
