"""
URL configuration for Dhermapixel project.

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
from django.urls import path, include
from .views import dhermapixel
from .views import promociones
from .views import tratamientos
from .views import contacto
from .views import inicioDeSesión
from .views import dermapen
from .views import prp
from .views import hialuronico
from .views import meso
from .views import mesoterapiaCapilar
from .views import criolipolisis
from .views import registro

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dhermapixel.as_view(), name="index"),
    path("promociones/", promociones.as_view(), name="promociones"),
    path("tratamientos/", tratamientos.as_view(), name="tratamientos"),
    path("contacto/", contacto.as_view(), name="contacto"),
    path("inicioDeSesion/", inicioDeSesión.as_view(), name="inicioDeSesión"),
    path("dermapen/", dermapen.as_view(), name="dermapen"),
    path("prp/", prp.as_view(), name="prp"),
    path("hialuronico/", hialuronico.as_view(), name="hialuronico"),
    path("meso/", meso.as_view(), name="meso"),
    path("mesoterapiaCapilar/", mesoterapiaCapilar.as_view(), name="mesoterapiaCapilar"),
    path("criolipolisis/", criolipolisis.as_view(), name="criolipolisis"),
    path("registro/", registro.as_view(), name="registro"),
    path('crud/', include('aplicaciones.Estetica.urls')),
    
]
