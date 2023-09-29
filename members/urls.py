from django.urls import path
from . import views

#Caminhos/Urls
urlpatterns = [
    path('cadastro', views.signup, name="signup"),
    path('login', views.signin, name="signin"),
    path('sair', views.signout, name="signout")
]
