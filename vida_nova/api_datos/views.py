# api_datos/views.py

from rest_framework.views import APIView
from rest_framework.response import Response  # ✅ Correcto
from .models import Paciente
from .serializers import PacienteSerializer  # ✅ correcto

import requests
from django.shortcuts import render
from requests.exceptions import RequestException


# 🔹 API REST con Django REST Framework
class PacienteListView(APIView):
    def get(self, request):
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 🔹 Vista para consumir la API y mostrar HTML
def consumir_api(request):
    try:
        response = requests.get("http://localhost:8001/api/")
        response.raise_for_status()
        pacientes = response.json()
    except RequestException as e:
        print("Error al consumir la API:", e)
        pacientes = []

    return render(request, "api_datos/pacientes.html", {"pacientes": pacientes})

