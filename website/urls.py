from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('members.urls')),
]
