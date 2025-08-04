from django.shortcuts import render

def indicators(request):
    return render(request, 'app_pages/indicators.html')
