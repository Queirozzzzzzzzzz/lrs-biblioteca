from django.contrib import admin
from .models import Book, UserLoan

admin.site.register(Book)
admin.site.register(UserLoan)