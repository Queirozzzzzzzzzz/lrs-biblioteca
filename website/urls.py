from django.urls import path, include
from . import views

#Adiciona as urls

urlpatterns = [
    path('', views.home, name="home"),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('members.urls')),
    path('cadastro-livros', views.booksignup, name="booksignup"),
    path('livros/', views.books, name="books"),
    path('equipe/', views.groupmembers, name="groupmembers"),
]
