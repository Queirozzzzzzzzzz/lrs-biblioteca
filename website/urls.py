from django.urls import path, include
from . import views

#Adiciona as urls

urlpatterns = [
    path('', views.home, name="home"),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('members.urls')),
    path('cadastro-livros', views.bookadd, name="bookadd"),
    path('cadastro-livros/procurar', views.booksearch, name="booksearch"),
    path('livros/', views.books, name="books"),
    path('edicao-livros/', views.bookedit, name="bookedit"),
    path('emprestimos/', views.loans, name="loans"),
    path('meus-emprestimos/', views.myloans, name="myloans"),
    path('perfil/', views.profile, name="profile"),
    path('loanlist/<int:book_id>/', views.loanslist, name="loanslist"),
    path('livros/emprestimo', views.bookloan, name="bookloan")
]
