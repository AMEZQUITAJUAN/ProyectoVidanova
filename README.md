# VidaNova -
**Repositorio del sistema web desarrollado para la IPS VidaNova**, diseñado para optimizar el registro, seguimiento y gestión de datos de pacientes oncológicos, con integración a la plataforma externa SIISA y un tablero de control para supervisores y agentes.

## 🚀 Características Principales

- Registro y gestión de pacientes oncológicos.
- Acceso por roles: agentes, supervisores, líderes.
- Integración con SIISA para extracción de datos externos.
- Generación de reportes y seguimiento de citas.
- Sistema de alertas y observaciones internas.
- Tablero de control interactivo.

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python + Django
- **Base de datos**: SQLite (DB Browser) o PostgreSQL (opcional)
- **Control de versiones**: Git + GitHub
- **Prototipado**: Figma, Canva
- **Documentación**: Google Docs + Sheets

## 📂 Estructura del Proyecto


## 📊 Flujo General del Proyecto

1. **Mes 1**: Análisis de requerimientos, entrevistas y arquitectura.
2. **Mes 2**: Diseño de base de datos, wireframes, validación con usuarios.
3. **Mes 3**: Desarrollo del MVP (formulario principal + login).
4. **Mes 4**: Funcionalidades avanzadas (reportes, seguimientos).
5. **Mes 5**: Pruebas, simulaciones y conexión a SIISA.
6. **Mes 6**: Despliegue, capacitación y entrega formal.

## ✅ Requisitos para ejecutar el proyecto

- Python 3.10+
- Django 4.x
- DB Browser (SQLite) o PostgreSQL
- Git
- Navegador web moderno

## ▶️ Cómo ejecutar localmente

```bash
git clone https://github.com/tuusuario/VidaNova.git
cd VidaNova
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
