from django import forms
from django.forms import ModelForm
from .models import Book, UserLoan

#Formulário do livro
class BookRegistrationForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'synopsis', 'release_date', 'is_available', 'stock','front_cover')


# Formulário de empréstimo
class UserLoanForm(forms.ModelForm):
    class Meta:
        model = UserLoan
        fields = ['date', 'book', 'user']

