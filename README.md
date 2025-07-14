# 📊 Sistema Web de Gestión Oncológica - IPS VidaNova

Este proyecto es una aplicación web desarrollada con Django para optimizar el registro, seguimiento y generación de reportes de pacientes oncológicos. Fue diseñado para mejorar los procesos actuales de la IPS VidaNova, reemplazando tareas manuales y duplicadas en herramientas como Excel y SIISA.

---

## ⚙️ Tecnologías

- 🐍 Python 3.x
- 🕸️ Django
- 🗃️ SQLite
- 🧪 HTML + CSS (Frontend simple)
- 🧠 VS Code
- 🧰 Herramientas adicionales: Git, GitHub, DB Browser for SQLite

---

## 🚀 Funcionalidades (MVP)

- Registro de pacientes con información clínica y administrativa
- Agenda médica por especialidad
- Seguimiento clínico por etapas (diagnóstico, tratamiento, control)
- Reportes descargables en Excel o PDF
- Autocompletado y validaciones inteligentes
- Panel de control con indicadores (dashboard)
- Control de usuarios y roles

---

## 🔐 Roles definidos

- **Navegador**: Registra información inicial
- **Supervisor**: Revisa y valida reportes
- **Asistencial**: Gestión clínica
- **Administrativo**: Planificación y autorizaciones

---

## 🧩 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # o env\Scripts\activate en Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta migraciones y el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
🛠️Guía Básica del Proyecto VidaNova en Django
📁 1. Crear entorno virtual: python -m venv virtual
📁2. Activar el entorno virtual En Windows:virtual\Scripts\activate
🐍 3. Instalar Django: python -m pip (install django: pip install django)
🔎 4. Verificar la versión de Django
Opción 1: python
>>> import django
>>> print(django.get_version())
>>> quit()
Opción 2: python -m django --version
🚧 5. Crear el proyecto Django: 
django-admin startproject vida_nova
cd vida_nova
🚀 6. Ejecutar el servidor: python manage.py runserver.
Abre en el navegador: http://127.0.0.1:8000
📄 7. Crear archivo views.py (dentro de la carpeta vida_nova)
from django.http import HttpResponse
def homepage(requess):
    return HttpResponse("Hola amegis de vidanova!")
def about(request):
    return HttpResponse("Esta es la pagina de acerca de vidanova!")

🌐 8. Configurar las rutas en urls.py (archivo dentro de la carpeta vida_nova):
Nota:La página principal va con view.homepages
y abouts/ va con view.abouts

from django.contrib import admin
from django.urls import path
from . import views as view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage),
    path('about/',view.about),
]

📌 Accede a:
Página principal → http://127.0.0.1:8000/
Página “acerca de” → http://127.0.0.1:8000/about/
Nota:Para correr el programa nuevamente refresca la página o ejecuta python runserver y para cargar  la vista abouts se pone(/about/)
🧱 9. Configurar settings.py para usar la carpeta de templates
En settings.py, busca la sección de TEMPLATES y modifica así:
'DIRS': [BASE_DIR / 'templates'],
Esto permitirá usar una carpeta templates/ para tus archivos HTML personalizados.

---

## 📂 Estructura del Proyecto

```
core/
│
├── registro/             # Aplicación principal
│   ├── models.py         # Modelos de base de datos
│   ├── views.py          # Vistas
│   ├── templates/        # HTMLs
│   └── ...
├── core/                 # Configuración general del proyecto
│   └── settings.py
├── manage.py
└── README.md
```

---

## 🗃️ Base de datos

Se utiliza SQLite durante la fase inicial del proyecto para facilitar el desarrollo local.

---

## ✍️ Autor

Desarrollado por Juan José Amezquita Dussan* para el proyecto de modernización de la IPS VidaNova.

---

## 📌 Estado del proyecto

🚧 En desarrollo: se encuentra en la fase de implementación del modelo de datos y prototipo de funcionalidades clave.
