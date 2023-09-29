from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    #Organiza a ordem dos componentes
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
