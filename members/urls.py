from django.urls import path
from . import views

#Caminhos/Urls
urlpatterns = [
    path('login', views.signin, name="signin"),
    path('registro-usuario/', views.userregister, name="userregister"),
    path('sair', views.signout, name="signout")
]
