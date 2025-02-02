from django.shortcuts import render,redirect
from .forms import RegistroForm,login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    return render(request,'index.html')

#def Registro(request):
 #   return render(request,'Formularios.html')
def Registro(request):
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                form.add_error('username','El usuario ya existe.')
            else:
                User.objects.create_user(username=username,email=email,password=password)
                return redirect('index')
    else:
        form = RegistroForm()
    return render(request,"registro.html",{"form": form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
        error = "Nombre de usuario o contraseña incorrectos."
        return render(request, 'login.html', {'form': form, 'error': error})
    return render(request, 'login.html', {"form": form}) 

def logout_view(request):
    logout(request)
    return redirect('index')