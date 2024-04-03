from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect
from .models import Material
from .forms import MaterialForm

def lista_materiais(request):
    materiais = Material.objects.all()
    return render(request, 'lista_materiais.html', {'materiais': materiais})

def adiciona_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_materiais')
    else:
        form = MaterialForm()
    return render(request, 'adiciona_material.html', {'form': form})

def edita_material(request, pk):
    material = Material.objects.get(pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('lista_materiais')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'edita_material.html', {'form': form})

def deleta_material(request, pk):
    material = Material.objects.get(pk=pk)
    material.delete()
    return redirect('lista_materiais')
