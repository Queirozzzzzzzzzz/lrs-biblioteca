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
    path('emprestimos/lista/<int:book_id>/', views.loanslist, name="loanslist"),
    path('emprestimos/lista/expirados/<int:book_id>/', views.expiredloanslist, name="expiredloanslist"),
    path('emprestimos/lista/ativos/<int:book_id>/', views.activeloanslist, name="activeloanslist"),
    path('livros/emprestimo', views.bookloan, name="bookloan"),
    path('pdf/<int:loan_id>/', views.receiptpdfview, name='receiptpdfview'),
    path('encerrar-emprestimo/<int:loan_id>', views.endloan, name="endloan"),
    path('lista-de-desejos/', views.wishlistadd, name="wishlistadd")
]
