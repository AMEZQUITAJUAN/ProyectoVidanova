import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form.add_error(None, "Usuario o contraseña incorrectos")
        
    return render(request, 'login.html', {'form': form})

def homepage(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def consumir_api(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
    except requests.exceptions.RequestException as e:
    
        data = {"error": f"An error occurred al consumir a API: {e}"}
        
    return render(request, 'api_resultados.html', {'data': data})
