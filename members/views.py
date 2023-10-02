from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

#Funções

#Cadastro/login de usuário
def signup_signin(request):
    #Previne um usuário logado de se cadastrar
    if request.user.is_authenticated:
        return redirect('home')
    
    form = SignUpForm()

    #Checa se formulário "POST" foi chamado
    if request.method == "POST":

        #Checa se formulário é de cadastro
        if "signup" in request.POST:
            
            #Obtém os dados do formulário
            form = SignUpForm(request.POST)

            #Checa se form é válido e loga o usuário com a conta criada
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                passwd = form.cleaned_data['password1']
                user = authenticate(username=username, password=passwd)
                login(request, user)
                messages.success(request, ("Registrado com sucesso!"))
                return redirect('home')
            #Mostra mensagens de erro e recarrega a página
            else:
                for error in form.errors:
                    messages.success(request, form.errors[error])
                return render(request, 'authenticate/login.html', {
                    
                })
        
        elif "signin" in request.POST:
            
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
                return render(request, 'authenticate/login.html', {
                    
                })

    #Carrega página de login
    return render(request, 'authenticate/login.html', {
        
    })

def signout(request):
    logout(request)
    messages.success(request, ("Você saiu de sua conta"))
    return redirect('home')