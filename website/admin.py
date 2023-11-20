from django.contrib import admin
from .models import Book, UserLoan, HistoryUserLoan, UserWishList

admin.site.register(Book)
admin.site.register(UserLoan)
admin.site.register(HistoryUserLoan)
admin.site.register(UserWishList)