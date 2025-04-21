from django.shortcuts import render, get_object_or_404
from .models import Cliente

def clientes(request):
  return render(request, 'clientes/clientes.html', {
    'clientes': Cliente.objects.all(),
  })

def cliente(request, id):
  return render(request, 'clientes/cliente.html', {
    'cliente': get_object_or_404(Cliente, id=id),
  })