from django.urls import path, include
from . import views

#Adiciona as urls

urlpatterns = [
    path('', views.home, name="home"),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('members.urls')),
    path('cadastro-livros', views.bookadd, name="bookadd"),
    path('livros/', views.books, name="books"),
    path('edicao-livros/', views.bookedit, name="bookedit"),
    path('emprestimos/', views.loans, name="loans"),
    path('meus-emprestimos/', views.myloans, name="myloans"),
    path('profile/', views.profile, name="profile"),
    path('lista-emprestimos/', views.loanslist, name='loanslist'),
]
