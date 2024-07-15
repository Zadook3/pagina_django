from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, InstrumentoForm
from django.contrib.auth import authenticate, login
from instrumentos.models import Instrumento
from django.contrib import messages




def index(request):
    return render(request, 'index.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def agregar_instrumento(request):

    data = {
        'form': InstrumentoForm() 
    }

    if request.method == 'POST':
        formulario = InstrumentoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/instrumento/agregar.html', data)

def listar_instrumentos(request):
    instrumentos = Instrumento.objects.all()

    data = {
        'instrumentos': instrumentos
    }
    return render(request, 'app/instrumento/listar.html', data)

def modificar_instrumento(request, id):

    instrumento = get_object_or_404(Instrumento, id=id)

    data = {
        'form': InstrumentoForm(instance=instrumento)
    }
    
    if request.method == 'POST':
        formulario = InstrumentoForm(data=request.POST, instance=instrumento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_instrumentos")
        data["form"] = formulario

    return render(request, 'app/instrumento/modificar.html', data)

def eliminar_instrumento(request, id):
    instrumento = get_object_or_404(Instrumento, id=id)
    instrumento.delete()
    return redirect(to="listar_instrumentos")
    


