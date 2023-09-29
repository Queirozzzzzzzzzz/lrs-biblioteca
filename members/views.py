from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

#Método de cadastro
def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            passwd = form.cleaned_data['password1']
            user = authenticate(username=username, password=passwd)
            login(request, user)
            messages.success(request, ("Registrado com sucesso!"))
            return redirect('home')
        else:
            messages.success(request, ("Houve um erro no seu registro"))
            return render(request, 'authenticate/signup.html', {
                'form':form,
            })
    else:

        return render(request, 'authenticate/signup.html', {
            'form':form,
        })

#Método de login
def signin(request):
    #Confere se o método que foi solicitado é do tipo "POST"
    if request.method == "POST":
        #Obtém os dados do formulário
        user_login = request.POST['user_login']
        password = request.POST['password']

        #Sistema do django de autenticação com os dados obtidos
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            #Login com a autenticação do django e redireciona para a homepage
            login(request, user)
            return redirect('home')
        else:
            #Mensagem de erro e redireciona novamente para a página de login
            messages.success(request, ("Houve um erro ao logar na sua conta, tente novamente..."))
            return redirect('signin')

    else:
        #Renderiza a página de login
        return render(request, 'authenticate/signin.html', {})

def signout(request):
    logout(request)
    messages.success(request, ("Você saiu de sua conta"))
    return redirect('home')