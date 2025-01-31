from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label="Usuario",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    email = forms.EmailField(label="Correo electronico")