from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookRegistrationForm
from .models import Book
import requests
from dateutil.parser import parse
from django.core.files.base import ContentFile
from django.conf import settings

# Funções

# Página inicial
@login_required(login_url='/membros/login')
def home(request):
    return render(request, 'home.html', {})

# Cadastro de livros
@staff_member_required
def bookadd(request):
    if request.method == "POST":
        # Verifica se a ação é para adicionar um novo livro
        if request.POST.get("form_action") == "add_new_book":
            form = BookRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                book = form.save(commit=False)
            # Se um arquivo de capa foi enviado salvar ele
            if 'front_cover' in request.FILES:
                book.front_cover = request.FILES['front_cover']
            # Se uma URL de imagem foi fornecida, baixa a imagem e a salva
            elif 'image_url' in request.POST and request.POST['image_url']:
                image_file = download_image(request.POST['image_url'])
                if image_file is not None:
                    book.front_cover.save('image.jpg', image_file)
            # Se nenhum arquivo de capa foi enviado e nenhuma URL de imagem foi fornecida, salva a imagem padrão
            else:
                book.front_cover.save('default_image.jpg', get_default_image())
            book.save()
            return redirect('books')
        
        # Verifica se a ação é para pegar a informação do livro
        elif request.POST.get("form_action") == "get_book_info":
            book_title = request.POST['book_title']
            # Chama uma função para buscar informações do livro usando a API do Google Books
            book_info = get_book_info(book_title)
            form = BookRegistrationForm(initial={})
            return render(request, 'book-signup.html', {'book_info': book_info})
    
    form = BookRegistrationForm()
    return render(request, 'book-signup.html', {"form": form})

# Edição de livros
@staff_member_required
def bookedit(request):
    form = BookRegistrationForm()
    return render(request, 'book-edit.html', {"form": form})

# Empréstimo de livros
@staff_member_required
def bookloan(request):
    if request.method == "POST":
        form = BookRegistrationForm(request.POST, request.FILES)
    form = BookRegistrationForm()
    return render(request, 'book-signup.html', {"form": form})

# Livros
@login_required(login_url='/membros/login')
def books(request):
    all_books = Book.objects.all
    return render(request, "books.html", {"all_books":all_books})

# Empréstimo
@login_required(login_url='/membros/login')
def loans(request):
    return render(request, "loans.html", {})

# Meus Empréstimos
@login_required(login_url='/membros/login')
def myloans(request):
    return render(request, "my-loans.html", {})

# Cadastro de usuário
@staff_member_required
def userregister(request):
    return render(request, "user-register.html", {})

# Perfil
@login_required(login_url='/membros/login')
def profile(request):
    return render(request, "profile.html", {})

# Lista de Empréstimos Solicitados
@staff_member_required
def loanslist(request):
    return render(request, "loans-list.html", {})

# Função para buscar informações do livro usando a API do Google Books
def get_book_info(book_title):
    # Define a URL base da API do Google Books
    base_url = 'https://www.googleapis.com/books/v1/volumes'

    # Define os parâmetros da solicitação, que é o título do livro
    params = {
        'q': f'intitle:{book_title}',
    }

    # Faz uma solicitação GET para a API do Google Books com os parâmetros definidos
    response = requests.get(base_url, params=params)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Converte a resposta da API em um objeto JSON
        data = response.json()
        # Verifica se a resposta contém itens
        if 'items' in data:
            # Obtém as informações do primeiro livro retornado pela API
            first_book = data['items'][0]['volumeInfo']
            # Obtém os links das imagens do livro
            image_links = first_book.get('imageLinks', {})

            # Variável com as informações do livro
            book_info = {
                'title': first_book.get('title', ''),  # Obtém o título do livro
                'author': ', '.join(first_book.get('authors', [''])),  # Obtém os autores do livro
                'description': first_book.get('description', ''),  # Obtém a descrição do livro
                'release_date': parse(first_book.get('publishedDate', '')).strftime('%Y-%m-%d') if 'publishedDate' in first_book else '',  # Obtém a data de publicação do livro
                'image_url': image_links.get('thumbnail', ''),  # Obtém a URL da imagem em miniatura do livro
            }
            
            return book_info
    
    return {}

# Função que retorna um arquivo de imagem a partir de uma url
def download_image(url):
   response = requests.get(url)
   if response.status_code == 200:
       return ContentFile(response.content)
   return None

# Função para obter a capa default para os livros
def get_default_image():
    default_image_path = settings.STATICFILES_DIRS[0] + '/images/default_front_cover.png'
    with open(default_image_path, 'rb') as default_image_file:
        default_image = ContentFile(default_image_file.read())
    return default_image
