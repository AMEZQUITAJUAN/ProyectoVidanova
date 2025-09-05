from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
def homepage(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
