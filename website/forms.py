from django import forms
from django.forms import ModelForm
from .models import Book, UserLoan
from members.models import User

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

# Formulário de atualizar perfil
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image', 'phone_number']

