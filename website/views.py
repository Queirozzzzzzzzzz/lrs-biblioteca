from django.shortcuts import render

#Carrega homepage
def home(request):
    return render(request, 'home.html', {})
