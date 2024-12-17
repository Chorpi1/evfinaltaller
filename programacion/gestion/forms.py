from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Formulario de Inicio de Sesión
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class CrearUsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    grupo = forms.ChoiceField(choices=[("Administradores", "Administradores"), ("Empleados", "Empleados")], label="Grupo")