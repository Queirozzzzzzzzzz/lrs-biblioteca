from django.urls import path
from . import views

#Caminhos/Urls
urlpatterns = [
    path('login', views.signin, name="signin"),
    path('usuario/registrar/', views.userregister, name="userregister"),
    path('sair', views.signout, name="signout"),
    path('usuario/editar/<int:user_id>/', views.editprofile, name="editprofile")
]
