from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Reparacion, PerfilUsuario
from .forms import ReparacionForm

def index(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'index.html', {'reparaciones': reparaciones})

def about(request):
    return render(request, 'about.html')

def perfil(request):
    return render(request, 'perfil.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def crear_reparacion(request):
    if request.method == 'POST':
        form = ReparacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReparacionForm()
    return render(request, 'crear_reparacion.html', {'form': form})

def editar_reparacion(request, pk):
    reparacion = get_object_or_404(Reparacion, pk=pk)
    if request.method == 'POST':
        form = ReparacionForm(request.POST, request.FILES, instance=reparacion)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReparacionForm(instance=reparacion)
    return render(request, 'editar_reparacion.html', {'form': form})

def eliminar_reparacion(request, pk):
    reparacion = get_object_or_404(Reparacion, pk=pk)
    if request.method == 'POST':
        reparacion.delete()
        return redirect('index')
    return render(request, 'confirmar_eliminacion.html', {'reparacion': reparacion})

