from django.shortcuts import render, redirect
from .models import Visita
from .forms import VisitaForm
import logging

# Create your views here.
def listar_visitas(request):
    visitas = Visita.objects.all()
    print(visitas)
    logging.info("Listando visitas.")
    return render(request, 'listar_visitas.html', {'visitas': visitas})

def crear_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            logging.info("Visita creada correctamente.")
            return redirect('listar_visitas')
    else:
        form = VisitaForm()
    return render(request, 'crear_visita.html', {'form': form})

def eliminar_visita(request, visita_id):
    visita = Visita.objects.get(id=visita_id)
    if request.method == 'POST':
        visita.delete()
        return redirect('listar_visitas')
    return render(request, 'eliminar_visita.html', {'visita': visita})

def confirmar_visita(request, visita_id):
    visita = Visita.objects.get(id=visita_id)
    if request.method == 'POST':
        visita.estado = 'Confirmada'
        visita.save()
        return redirect('listar_visitas')
    return render(request, 'confirmar_visita.html', {'visita': visita})

def confirmar_conformidad(request, visita_id):
    visita = Visita.objects.get(id=visita_id)
    if request.method == 'POST':
        visita.estado = 'Conformidad'
        visita.save()
        return redirect('listar_visitas')
    return render(request, 'confirmar_conformidad.html', {'visita': visita})