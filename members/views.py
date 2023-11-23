from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import UserForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required

User = get_user_model()

#Funções

# Login de usuário
def signin(request):
      
      # Se o usuário já estiver autenticado, redireciona para a página inicial
      if request.user.is_authenticated:
          return redirect('home')

      # Se a requisição for POST
      if request.method == "POST":
          email = request.POST['email']
          password = request.POST['password']

          # Autentica o usuário
          user = authenticate(request, email=email, password=password)
          # Se o usuário for autenticado com sucesso, faz login e redireciona para a página inicial
          if user is not None:
              login(request, user)
              return redirect('home')
          # Se a autenticação falhar, exibe uma mensagem de erro
          else:
              messages.error(request, ("Houve um erro ao logar na sua conta, tente novamente..."))
              return render(request, 'authenticate/login.html', {})

      return render(request, 'authenticate/login.html', {})

# Cadastro de usuário
def userregister(request):
    form = UserForm()

    # Se a requisição for POST
    if request.method == "POST":
        form = UserForm(request.POST)

        # Se o formulário for válido
        if form.is_valid():
            # Salva o formulário do usuário
            user = form.save()

            # Obtém a senha
            password = form.cleaned_data['password1']

            # Define a foto de perfil padrão
            user.profile_image.save('default_cover_image.jpg', get_default_image())

            # Salva o usuário
            user.save()

            # Define os dados para o e-mail
            subject = "Cadastro Realizado - Out Of Box Library"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]

            # Prepara os dados para preencher o modelo
            context = {
                "full_name": user.full_name,
                "email": user.email,
                "course": user.course,
                "password": password,
            }

            # Renderiza o conteúdo HTML do e-mail
            email_message = render_to_string("email-user-register-template.html", context)

            # Envia o e-mail
            send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)

            messages.success(request, ("Registrado com sucesso!"))
            return redirect('userregister')
        
        # Se o formulário não for válido, exibe as mensagens de erro e recarrega a página
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])

            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']

            return render(request, 'authenticate/user-registration.html', {
                'full_name': full_name,
                'email': email,
            })

    return render(request, 'authenticate/user-registration.html', {})

# Desloga da conta
def signout(request):
    logout(request)
    messages.success(request, ("Você saiu de sua conta"))
    return redirect('home')

# Obtem a foto de perfil padrão
def get_default_image():
    # Url da imagem
    default_image_path = settings.STATICFILES_DIRS[0] + '/images/default_profile_image.png'

    # Salva o conteúdo da imagem
    with open(default_image_path, 'rb') as default_image_file:
        default_image = ContentFile(default_image_file.read())

    return default_image

# Edita o perfil de usuário
@login_required(login_url='/membros/login')
def editprofile(request, user_id):
    user = User.objects.get(id=user_id)
    
    if request.method == "POST":

        # Campos formulário
        fields = ['full_name', 'email', 'phone_number', 'course', 'password', 'profile_image']

        # Checa se o campo é válido
        def is_valid_field(field):
            
            # Rejeita campo se não existe na resposta do formulário
            if field not in request.POST and field not in request.FILES:
                return False

            # Campos que podem estar vazios
            optional_fields = ['course', 'phone_number']

            # Obtém o valor do campo do formulário
            value = request.POST.get(field)

            # Permite campos opcionais serem salvos sem informação
            if field in optional_fields:
                return True

            # Permite campo de imagem ser aceito
            if field == 'profile_image' and not None:
                return True

            # Nega campos vazios
            if field not in optional_fields and not value:
                return False

            # Aceita campos restantes
            else:
                return True

        # Se o campo for válido atribui ele ao usuário
        for field in fields:
            if is_valid_field(field):
                # Obtém o valor atual e novo do campo
                new_value = request.POST.get(field)
                current_value = getattr(user, field)

                # Muda o valor do campo
                if new_value != current_value:
                    # Mensagem de sucesso
                    mensagem = field + " atualizado com sucesso!"

                    # Apenas muda o e-mail se for único
                    if field == 'email':
                        if User.objects.filter(email=new_value).exists():
                            messages.error(request, 'Email já existe.')
                            continue
                    
                    # Salva a senha de forma correta
                    if field == 'password':
                        user.set_password(new_value)
                        messages.success(request, mensagem)
                        continue

                    # Salva a imagem de perfil 
                    if field == 'profile_image':
                        new_image = request.FILES.get('profile_image')
                        if new_image:
                            user.profile_image = new_image
                            messages.success(request, mensagem)
                        continue

                    setattr(user, field, request.POST.get(field))
                    messages.success(request, mensagem)
        
        # Salva
        user.save()

        return redirect('profile')
    
    return render(request, 'user-edit.html', {'profile':user})
