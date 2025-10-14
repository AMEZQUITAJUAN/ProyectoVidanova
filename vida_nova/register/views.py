from django.shortcuts import render, redirect
from django.contrib.auth import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            from.save()
            messages.success(request, 'Account created successfully!')
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})