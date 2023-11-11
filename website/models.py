from django.db import models
from django.conf import settings

#Modelo do livro
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=80)
    synopsis = models.TextField()
    release_date = models.DateField()
    is_available = models.BooleanField()
    stock = models.IntegerField()
    loan_count = models.IntegerField(default=0)
    front_cover = models.ImageField(null=True, blank=True, upload_to="static/images/")

    #Nome do livro no banco de dados
    def __str__(self):
        return self.title
    
#Modelo do empréstimo
class UserLoan(models.Model):
    date = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loan") # Associa o campo book ao objeto do livro
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Associa o campo user ao objeto do usuário
    is_on = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name + " " + self.book.title
