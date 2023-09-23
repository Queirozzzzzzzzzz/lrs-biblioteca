from django.db import models

class Member(models.Model):
    #id is automatic created by django
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    occupation = models.CharField(max_length=11)
    passwd = models.CharField(max_length=200)

    def __str__(self):
        return self.occupation + ': ' + self.name
