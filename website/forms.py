from django import forms
from django.forms import ModelForm
from .models import Book

#Formulário do livro
class BookRegistrationForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'synopsis', 'release_date', 'is_available', 'front_cover')
