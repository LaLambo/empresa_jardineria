"""
URL configuration for empresa_jardineria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import listar_visitas, crear_visita, eliminar_visita, confirmar_conformidad, confirmar_visita

urlpatterns = [
    path('listar_visitas/', listar_visitas, name='listar_visitas'),
    path('crear_visita/', crear_visita, name='crear_visita'),
    path('eliminar_visita/<int:visita_id>/', eliminar_visita, name='eliminar_visita'),
    path('confirmar_visita/<int:visita_id>/', confirmar_visita, name='confirmar_visita'),
    path('confirmar_conformidad/<int:visita_id>/', confirmar_conformidad, name='confirmar_conformidad'),
]
