from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistroForm,login,PublicacionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Publicacion
from django.contrib.auth.decorators import login_required
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
                return redirect('pantalla')
        error = "Nombre de usuario o contraseña incorrectos."
        return render(request, 'login.html', {'form': form, 'error': error})
    return render(request, 'login.html', {"form": form}) 


def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def pantalla(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    
    usernameP = request.user.username
    return render(request,'pantalla.html',{
        'publicaciones':publicaciones, 
        'usernameP':usernameP
        })

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect('pantalla')
    else:
        form = PublicacionForm()
    return render(request, 'crear_publicacion.html',{'form':form})

@login_required
def perfil(request,username):
    user = get_object_or_404(User, username=username)
    Publicaciones = Publicacion.objects.filter(usuario=user).order_by('-fecha_creacion')
    personas = User.objects.all().order_by('username')
    return render(request,'perfil.html',{
        'user':user,
        'publicaciones':Publicaciones,
        'personas':personas
        })