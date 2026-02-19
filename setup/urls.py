"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_telemetria.api import viewsets

router = DefaultRouter()
router.register(r'marca', viewsets.MarcaViewSet, basename='marca')
router.register(r'modelo', viewsets.ModeloViewSet, basename='modelo')
router.register(r'veiculo', viewsets.VeiculoViewSet, basename='veiculo')
router.register(r'unidade-medida', viewsets.UnidadeMedidaViewSet, basename='unidademedida')
router.register(r'medicacao', viewsets.MedicacaoViewSet, basename='medicacao')
router.register(r'medicacao-veiculo', viewsets.MedicacaoVeiculoViewSet, basename='medicacaoveiculo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),          # ou path('api/', include(router.urls))
]
