from django.contrib import admin
from django.urls import path, include
from . import views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.login, name='login'),
    path('home/', view.homepage),
    path('about/',view.about),
    path('board/', include('indicadores.urls')),
    path('search/', include('search.urls')),
    path('grid/', include('grid_search.urls')),
    path('doctors/', include('doctors.urls')),
    path('mensajes/', include('mensajes.urls')),
    path('adminboard/', include('adminboard.urls')),
    path('api/', view.consumir_api, name='consumir_api'),
    path('api/patients/', include('api_datos.urls')),
]
