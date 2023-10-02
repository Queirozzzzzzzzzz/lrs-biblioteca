from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookRegistrationForm
from .models import Book

#Funções

#Página inicial
@login_required(login_url='/membros/login')
def home(request):
    return render(request, 'home.html', {})

#Cadastro de livros
@staff_member_required
def booksignup(request):

    if request.method == "POST":
        form = BookRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'book-signup.html', {})
    
    form = BookRegistrationForm()
    return render(request, 'book-signup.html', {"form": form})

def books(request):
    all_books = Book.objects.all
    return render(request, "books.html", {"all_books":all_books})