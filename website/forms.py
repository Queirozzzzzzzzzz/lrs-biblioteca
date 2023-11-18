from django import forms
from django.forms import ModelForm
from .models import Book, UserLoan

#Formulário do livro
class BookRegistrationForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'synopsis', 'genre', 'publisher', 'release_date', 'status', 'stock', 'origin', 'comment', 'front_cover')


# Formulário de empréstimo
class UserLoanForm(forms.ModelForm):
    class Meta:
        model = UserLoan
        fields = ['book', 'user']

