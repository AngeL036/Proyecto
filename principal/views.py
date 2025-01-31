from django.shortcuts import render
from .forms import RegistroForm
# Create your views here.
def index(request):
    return render(request,'index.html')

#def Registro(request):
 #   return render(request,'Formularios.html')
def Registro(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            print(f"Nuevo usuario registrado: {username} ({email})")
            return render(request, "registro_exito.html", {"username": username})
    return render(request,"registro.html",{"form": form})