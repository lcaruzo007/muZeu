from django.shortcuts import render, get_object_or_404
from .models import ObjetoMuseu

def lista_objetos(request):
    objetos = ObjetoMuseu.objects.all()
    return render(request, 'lista_objetos.html', {'objetos': objetos})

def detalhe_objeto(request, pk):
    objeto = get_object_or_404(ObjetoMuseu, pk=pk)
    return render(request, 'detalhe_objeto.html', {'objeto': objeto})
