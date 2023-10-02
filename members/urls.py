from django.urls import path
from . import views

#Caminhos/Urls
urlpatterns = [
    path('login', views.signup_signin, name="signup_signin"),
    path('sair', views.signout, name="signout")
]
