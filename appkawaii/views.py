from django.shortcuts import render, redirect 
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm 
from django.contrib import messages 
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User 
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.
def portada(request):
    return render(request, 'portada.html',{})

def registro(request):     
    if request.method == "POST":        
        nombre = request.POST["nombreuser"]       
        correo = request.POST["correo"]         
        clave =  request.POST["password"]        
        User.objects.create(username=nombre, email=correo, password=make_password(clave))         
        return redirect(settings.LOGIN_REDIRECT_URL1, request.path)  
    return render(request,'registro.html',{})

def principal(request):
    return render(request, 'principal.html',{})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/principal')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'login.html', {'form': form})
    
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/portada')
    
def  nosotros(request):
    return render(request, 'nosotros.html',{})
    
def  Admin(request):
    return render(request, 'Admin.html',{})
    
def index(request):
    return render(request, 'index.html',{})
    
def carro(request):
    return render(request, 'carro.html',{})

def Maui(request):
    return render(request, 'Maui.html',{})

def collokey(request):
    return render(request, 'collokey.html',{})
    

