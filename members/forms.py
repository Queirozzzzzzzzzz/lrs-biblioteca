from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulário de cadastro de usuário
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form'}))

    #Define os componentes
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
