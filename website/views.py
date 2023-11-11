from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookRegistrationForm, UserLoanForm
from .models import Book, UserLoan
import requests
from dateutil.parser import parse
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

User = get_user_model()

# Funções

# Página inicial
@login_required(login_url='/membros/login')
def home(request):
    return render(request, 'home.html', {})

# Adicionar novo livro
@staff_member_required
def bookadd(request):
   if request.method == "POST":
       form = BookRegistrationForm(request.POST, request.FILES)
       if form.is_valid():
           book = form.save(commit=False)
           if 'front_cover' in request.FILES:
               book.front_cover = request.FILES['front_cover']
           elif 'image_url' in request.POST and request.POST['image_url']:
               image_file = download_image(request.POST['image_url'])
               if image_file is not None:
                  book.front_cover.save('cover.jpg', image_file)
           else:
               book.front_cover.save('default_cover_image.jpg', get_default_image())
           book.save()
           return redirect('bookadd')
   form = BookRegistrationForm()
   return render(request, 'book-signup.html', {"form": form})

# Procura livro
@staff_member_required
def booksearch(request):
   if request.method == "POST":
       book_title = request.POST['book_title']
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
@login_required(login_url='membros/login')
def bookloan(request):
    # Valores do form
    book_id = request.POST.get('book')
    user_id = request.POST.get('user')

    # Busca livro e usuário
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)

    # Checa se usuário já registrou o livro
    bookalreadyregistered = UserLoan.objects.filter(user=user, book=book).exists()

    if request.method == "POST":
        form = UserLoanForm(request.POST)
        if form.is_valid():
            if bookalreadyregistered:
                messages.error(request, ("Livro já registrado em seus empréstimos"))
                return redirect('books')
            else:
                # Define valores do form
                userloan = form.save(commit=False)
                userloan.date = timezone.now()
                userloan.book = book
                userloan.user = user
                book.loan_count += 1

                userloan.save()
            return redirect('myloans')

    return redirect('books')


# Livros
@login_required(login_url='/membros/login')
def books(request):
    all_books = Book.objects.all
    return render(request, "books.html", {"all_books":all_books})

# Livros com empréstimos
@login_required(login_url='/membros/login')
def loans(request):
    all_loans = UserLoan.objects.all()

    # Obtém os livros dos empréstimos com o campo "is_on" desativado
    books = [loan.book for loan in all_loans if loan.is_on is not True]

    # Remove as duplicações dos livros
    books = list(set(books))

    return render(request, "loans.html", {"books":books})

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
def loanslist(request, book_id):
    # Obtém o livro
    book = get_object_or_404(Book, id=book_id)

    # Obtém os empréstimos
    book_loans = book.loan.all()

    # Checa se estoque do livro é maior que 0
    if book.stock > 0:
        
        # Ordena os empréstimos por data de solicitação
        book_loans.order_by('date')

        # Aceitar ou negar empréstimo
        if request.method == "POST":
            # Resposta do form
            accept = request.POST.get("accept")
            reject = request.POST.get("reject")
            
            # Aceitar livro
            if accept is not None:
                # Obtém o empréstimo
                loan = UserLoan.objects.get(pk=accept)

                # Ativa empréstimo
                loan.is_on = True
                loan.save()

                # Diminui estoque do livro
                book.stock -= 1
                book.save()

                # Envia um email de notificação
                sendemail("Empréstimo Aceito - Out Of Box Library", [loan.user.email], "email-accept-loan.html", context = {"user": loan.user, "book":book})

                return redirect('loanslist', book_id=book_id)

            # Negar livro
            if reject is not None:
                # Obtém o empréstimo
                loan = UserLoan.objects.get(pk=reject)
    else:
        # Obtém empréstimos para serem removidos
        remove_loans = UserLoan.objects.filter(book_id=book_id, is_on=False)

        # Envia e-mail/notificação sobre negação do empréstimo
        for loan in remove_loans:
            # Envia um email de notificação
            sendemail("Empréstimo Negado - Out Of Box Library", [loan.user.email], "email-reject-loan.html", context = {"user": loan.user, "book":book})

        remove_loans.delete()

    return render(request, "loans-list.html", {"book":book, "book_loans":book_loans})

# Enviar e-mail
def sendemail(subject, recipient_list, email_template,context):
    # Email de envio
    from_email = settings.EMAIL_HOST_USER

    # Renderiza o conteúdo HTML do e-mail
    email_message = render_to_string(email_template, context)

    # Envia o e-mail
    send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)

# Buscar informações do livro usando a API do Google Books
def get_book_info(book_title):
    # Define a URL base da API do Google Books
    base_url = 'https://www.googleapis.com/books/v1/volumes'

    # Define os parâmetros da solicitação
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

# Retorna um arquivo de imagem a partir de uma url
def download_image(url):
    # Url da imagem
    response = requests.get(url)

    # Se retornou uma imagem retorna o conteúdo da imagem
    if response.status_code == 200:
        return ContentFile(response.content)
    
    return None

# Obtem a capa padrão para os livros
def get_default_image():
    # Url da imagem
    default_image_path = settings.STATICFILES_DIRS[0] + '/images/default_front_cover.png'

    # Salva o conteúdo da imagem
    with open(default_image_path, 'rb') as default_image_file:
        default_image = ContentFile(default_image_file.read())

    return default_image
