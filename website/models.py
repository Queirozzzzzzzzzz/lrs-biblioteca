from django.db import models
from django.conf import settings
from django.db.models.functions import Now

# Modelo do livro
class Book(models.Model):
    added_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=80)
    synopsis = models.TextField()
    GENRE_CHOICES = [
    ('antiques & collectibles', 'Antiguidades & Colecionáveis'),
    ('literary collections', 'Coleções Literárias'),
    ('architecture', 'Arquitetura'),
    ('literary criticism', 'Crítica Literária'),
    ('art', 'Arte'),
    ('mathematics', 'Matemática'),
    ('bibles', 'Bíblias'),
    ('medical', 'Médico'),
    ('biography & autobiography', 'Biografias & Autobiografias'),
    ('music', 'Música'),
    ('body, mind & spirit', 'Corpo, Mente & Espírito'),
    ('nature', 'Natureza'),
    ('business & economics', 'Negócios & Economia'),
    ('performing arts', 'Artes Performáticas'),
    ('comics & graphic novels', 'Quadrinhos & Romances Gráficos'),
    ('pets', 'Animais de Estimação'),
    ('computers', 'Computadores'),
    ('philosophy', 'Filosofia'),
    ('cooking', 'Culinária'),
    ('photography', 'Fotografia'),
    ('crafts & hobbies', 'Artesanato & Hobbies'),
    ('poetry', 'Poesia'),
    ('design', 'Design'),
    ('political science', 'Ciência Política'),
    ('drama', 'Drama'),
    ('psychology', 'Psicologia'),
    ('education', 'Educação'),
    ('reference', 'Referência'),
    ('family & relationships', 'Família & Relacionamentos'),
    ('religion', 'Religião'),
    ('fiction', 'Ficção'),
    ('science', 'Ciência'),
    ('foreign language study', 'Estudo de Idiomas'),
    ('self-help', 'Autoajuda'),
    ('games & activities', 'Jogos & Atividades'),
    ('social science', 'Ciência Social'),
    ('gardening', 'Jardinagem'),
    ('sports & recreation', 'Esportes & Lazer'),
    ('health & fitness', 'Saúde & Fitness'),
    ('study aids', 'Apoios de Estudo'),
    ('history', 'História'),
    ('technology & engineering', 'Tecnologia & Engenharia'),
    ('house & home', 'Casa & Lar'),
    ('transportation', 'Transporte'),
    ('humor', 'Humor'),
    ('travel', 'Viagem'),
    ('juvenile fiction', 'Ficção Juvenil'),
    ('true crime', 'Crime Verdadeiro'),
    ('juvenile nonfiction', 'Não Ficção Juvenil'),
    ('young adult fiction', 'Ficção para Jovens Adultos'),
    ('language arts & disciplines', 'Artes da Linguagem & Disciplinas'),
    ('young adult nonfiction', 'Não Ficção para Jovens Adultos'),
    ('law', 'Direito'),
    ]
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField()
    STATUS_CHOICES = [
       ('available', 'Disponível'),
       ('unavailable', 'Indisponível'),
       ('soon', 'Em Breve'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    stock = models.IntegerField()
    ORIGIN_CHOICES = [
        ('bought', 'Comprado'),
        ('donated', 'Doado'),
        ('unknown', 'Não especificado'),
    ]
    origin = models.CharField(max_length=12, choices=ORIGIN_CHOICES, default='unknown')
    comment = models.TextField(null=True, blank=True)
    loan_count = models.IntegerField(default=0)
    front_cover = models.ImageField(null=True, blank=True, upload_to="static/images/")

    #Nome do livro no banco de dados
    def __str__(self):
        return self.title
    
# Modelo do empréstimo
class UserLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loan") # Associa o campo book ao objeto do livro
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Associa o campo user ao objeto do usuário
    is_on = models.BooleanField(default=False)
    start_date = models.DateField()
    final_date = models.DateField()
    renews = models.IntegerField(default=1)

    def __str__(self):
        return self.user.full_name + " " + self.book.title

# Modelo do empréstimo para histórico
class HistoryUserLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="history_loan") # Associa o campo book ao objeto do livro
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Associa o campo user ao objeto do usuário
    start_date = models.DateField()
    final_date = models.DateField()

    def __str__(self):
        return self.user.full_name + " " + self.book.title  

# Modelo de Lista de Desejos        
class UserWishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Associa o campo user ao objeto do usuário
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.user.full_name