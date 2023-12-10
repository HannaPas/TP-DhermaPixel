
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarPaciente/', views.registrarPaciente, name='registrarPaciente'),
    path('editarPaciente/<id>', views.editarPaciente),
    path('eliminarPaciente/<id>', views.eliminarPaciente),
    path('edicionPaciente/', views.edicionPaciente)
   
]