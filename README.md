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
Proyecto Vidanova:
Espacio virtual: python -m venv virtual
Acceder: virtual/Scripts/activate
Instalar Django: python -m pip install django
Forma de ver la versión de django: python  
>>> import django
>>> print(django.get_version())
>>> quit()
Otro forma: python -m django --version
crear proyecto: django-admin startproject vida_nova
Entrar a la carpeta: cd vida_nova
Para correr el proyecto: python manage.py runserver
Crear archivo views.py en la carpeta vidanova:
from django.http import HttpResponse
def homepage(requess):
    return HttpResponse("Hola amegis de vidanova!")
def about(request):
    return HttpResponse("Esta es la pagina de acerca de vidanova!")

13. La página principal va con views. homepages
y abouts/ va con view.abouts

from django.contrib import admin
from django.urls import path
from . import views as view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage),
    path('about/',view.about),
]

para correr el programa nuevamente refresca la página o ejecuta python runserver y para cargar  la vista abouts se pone(/about/)

14. configiras settings.py en el apartado templates, en dirs: poner templates

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
