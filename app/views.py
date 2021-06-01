from django.core import paginator
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto
from .forms import ContactoForm, ProductoForm, RegistroUsuarioForm, SuscripcionForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializers, MarcaSerializers


# Create your views here.

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializers

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')
        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        else:
            return productos


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos,
        'formsus':SuscripcionForm()
    }

    if request.method=='POST':
        formulario = SuscripcionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = messages.success(request, "Estas suscrito")
            return redirect(to="home")
        else:
            data["formsus"] = formulario

    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'Form': ContactoForm(),
        'formsus':SuscripcionForm(),
        'formsus':SuscripcionForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["Form"] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    data = {
        'formsus':SuscripcionForm()
    }
    return render(request, 'app/galeria.html', data)

@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'Form': ProductoForm(),
        'formsus':SuscripcionForm()
    }

    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
        else:
            data["Form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'formsus':SuscripcionForm(),
        'entity':productos,
        'paginator':paginator
    }

    return render(request, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto),
        'formsus':SuscripcionForm()
    }

    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar")


def resgistro(request):
    data = {
        "form":RegistroUsuarioForm()
    }

    if request.method=='POST':
        formulario=RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'registration/registro.html', data)
