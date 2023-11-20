from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Formulário de Usuário
class UserForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, error_messages={'unique': 'Um usuário com este nome já existe.'})
    email = forms.EmailField(max_length=255, error_messages={'unique': 'Um usuário com este nome já existe.'})

    class Meta:
        model = User
        fields = ['full_name', 'email', 'course', 'phone_number', 'password1', 'password2']
