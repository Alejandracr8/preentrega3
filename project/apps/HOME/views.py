from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import is_valid_path

from .models import Cilindro, BodegaPrincipal, BodegaProveedor, Cliente
from .forms import CilindroForm, BodegaPrincipalForm, BodegaProveedorForm, ClienteForm

# Create your views here.
def index (request):
    context =  {'cilindro': CilindroForm, 'bodega_proveedor': BodegaProveedorForm, 'bodega_principal': BodegaPrincipalForm, 'cliente': ClienteForm}
    return render (request, "HOME/index.html", context )


def home (request):
    registro_cilindros = Cilindro.objects.all()
    registro_BodegaProveedor = BodegaProveedor.objects.all()
    registro_BodegaPrincipal = BodegaPrincipal.objects.all()
    Registro_Clientes = Cliente.objects.all()
    contexto = {'cilindro': registro_cilindros, 'Bodega Proveedor': registro_BodegaProveedor, 'Bodega Principal': registro_BodegaPrincipal, 'cliente': Registro_Clientes}
    return render (request, 'HOME/index.html', contexto)



def crear_cilindro(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        ...
    else:
        form = CilindroForm()
    return render (request, 'HOME/crear.html', {'form': form})

def crear_BodegaProveedor (request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = BodegaProveedorForm
        if form.is_valid():
            form.save()
        return redirect("crear:home")
    else:  # request.method == "GET"
        form = BodegaProveedorForm()
        return render (request, 'HOME/crear.html', {'form': form})
    
def crear_BodegaPrincipal(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        ...
    else:
        form = BodegaPrincipalForm()
    return render (request, 'HOME/crear.html', {'form': form})

def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        ...
    else:
        form = ClienteForm()
    return render (request, 'HOME/crear.html', {'form': form}) 