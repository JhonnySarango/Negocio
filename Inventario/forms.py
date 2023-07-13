from django import forms
from .models import libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class LibroForm(forms.ModelForm):
    class Meta:
        model=libro
        fields = ['nombre_libro','nombre_autor','categoria','Precio','codigo']
        labels = {
            'nombre_libro': 'Nombre_libro',
            'nombre_autor': 'Nombre_autor',
            'categoria': 'Categoria',
            'Precio': 'Precio',
            'codigo': 'Codigo'
        }
        widgets = {
            'nombre_libro': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_autor': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'Precio': forms.NumberInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'})
        }

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}