from django.contrib import admin
from .models import Book, UserLoan, HistoryUserLoan

admin.site.register(Book)
admin.site.register(UserLoan)
admin.site.register(HistoryUserLoan)