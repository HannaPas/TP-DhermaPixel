from django.shortcuts import render, redirect
from .models import Pacientes

# Create your views here.

def home(request):
    Listadopacientes = Pacientes.objects.all()
    return render(request, "gestionPacientes.html", {"pacientes": Listadopacientes })

def registrarPaciente(request):
    id = request.POST['txtID']
    nombre = request.POST['txtNombre']
    tratamiento = request.POST['txtTratamiento']
    precio = request.POST['txtPrecio']
    telefono = request.POST['txtTelefono']
    fecha = request.POST['txtFecha']

    pacientes = Pacientes.objects.create(
        id=id, nombre=nombre, tratamiento=tratamiento, precio=precio, telefono=telefono, fecha=fecha
    )

    return redirect('/crud')

def editarPaciente(request, id):
    paciente = Pacientes.objects.get(id=id)
    return render(request, "edicionPaciente.html", {"paciente": paciente})

def edicionPaciente(request):
    id = request.POST['txtID']
    nombre = request.POST['txtNombre']
    tratamiento = request.POST['txtTratamiento']
    precio = request.POST['txtPrecio']
    telefono = request.POST['txtTelefono']
    fecha = request.POST['txtFecha']

    paciente = Pacientes.objects.get(id=id)
    paciente.nombre = nombre
    paciente.tratamiento = tratamiento
    paciente.precio = precio
    paciente.telefono = telefono
    paciente.fecha = fecha

    paciente.save()

    return redirect('/crud')

def eliminarPaciente(request, id):
    paciente = Pacientes.objects.get(id=id)
    paciente.delete()

    return redirect('/crud')