from django.contrib import admin
from django.urls import path
from . import views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage),
    path('about/',view.about),
]
