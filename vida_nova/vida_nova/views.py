import requests
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
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
