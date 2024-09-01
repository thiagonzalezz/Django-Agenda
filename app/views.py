from django.shortcuts import render
from .models import Agenda

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['email']
        mensaje = request.POST['mensaje']
        agenda = Agenda(nombre=nombre, correo=correo, mensaje=mensaje)
        agenda.save()
        agendas = Agenda.objects.all()
        return render(request, 'base.html', {
            'agendas':agendas
        })
    else:
        return render(request, 'base.html')
    