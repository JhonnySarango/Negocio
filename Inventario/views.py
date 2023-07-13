from django.shortcuts import render,redirect
from .models import libro
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LibroForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'Inventario/index.html', {
        'libro': libro.objects.all()
    })
def view_libro(request, id):
    Libro=libro.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
def add(request):
    if request.method ==  'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.cleaned_data['nombre_libro']
            nuevo_autor = form.cleaned_data['nombre_autor']
            categoria = form.cleaned_data['categoria']
            nuevo_precio = form.cleaned_data['Precio']
            nuevo_codigo = form.cleaned_data['codigo']

            nuevolibro = libro(
                nombre_libro = nuevo_libro,
                nombre_autor = nuevo_autor,
                categoria = categoria,
                Precio = nuevo_precio,
                codigo = nuevo_codigo,
                estado='A'
                
            )

            nuevolibro.save()
            return render(request, 'Inventario/add.html', {
                'form': LibroForm(),
                'success': True 
            })
    else:
        form = LibroForm()
        return render(request, 'Inventario/add.html',{
            'form': LibroForm(),
        })
def edita(request, id):
    if request.method == 'POST':
        Libro = libro.objects.get(pk=id)
        form = LibroForm(request.POST, instance=Libro)
        if form.is_valid():
            form.save()
            return render(request,'Inventario/edit.html', {
                'form':form,
                'success':True
            })
    else:
        Libro=libro.objects.get(pk=id)
        form = LibroForm(instance=Libro)
        return render(request,'Inventario/edit.html',{
            'form':form
        })  
        
def delete(request, id):
    if request.method == 'POST':
        Libro=libro.objects.get(pk=id)
        Libro.estado='I'
        Libro.save()
    return HttpResponseRedirect(reverse('index'))

def registra(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {usuario} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'Inventario/register.html', context)