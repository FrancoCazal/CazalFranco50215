from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Salada, Dulce, Bebida, Articulo
class SaladaForm(forms.ModelForm):
    class Meta:
        model=Salada
        fields=['titulo', 'tipo', 'ocasion', 'ingredientes', 'preparacion', 'imagenRecetaSalada']

class DulceForm(forms.ModelForm):
    class Meta:
        model=Dulce
        fields=['titulo', 'tipo', 'ocasion', 'ingredientes', 'preparacion', 'imagenRecetaDulce']
    
class BebidaForm(forms.ModelForm):
    class Meta:
        model=Bebida
        fields=['titulo', 'tipo', 'ocasion', 'ingredientes', 'preparacion', 'imagenRecetaBebida']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model=Articulo
        fields=['titulo', 'subtitulo', 'contenido', 'imagen']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model=User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)