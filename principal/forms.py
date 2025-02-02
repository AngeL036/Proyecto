from django import forms
from .models import Publicacion

class RegistroForm(forms.Form):
    username = forms.CharField(label="Usuario",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    email = forms.EmailField(label="Correo electronico")

class login(forms.Form):
    username = forms.CharField(label="Usuario",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['texto']