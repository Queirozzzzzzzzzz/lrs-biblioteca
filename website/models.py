from django.db import models

#Modelo do livro
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=80)
    synopsis = models.TextField()
    release_date = models.DateField()
    is_available = models.BooleanField()
    front_cover = models.ImageField(null=True, blank=True, upload_to="static/images/")

    #Nome do livro no banco de dados
    def __str__(self):
        return self.title