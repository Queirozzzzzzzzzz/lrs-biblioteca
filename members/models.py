from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Gerenciador personalizado para o modelo de usuário
class UserManager(BaseUserManager):
    # Cria um usuário comum
    def create_user(self, email, full_name, phone_number, course, password=None):
        # Validação dos campos necessários
        if not email:
            raise ValueError("Usuário deve ter um email")
        if not full_name:
            raise ValueError("Usuário deve ter um nome completo")
        if not phone_number:
            raise ValueError("Usuário deve ter um número de telefone")
        if not course:
            raise ValueError("Usuário deve ter um curso")
        if not password:
            raise ValueError("Usuário deve ter uma senha")
    
        # Criação do usuário
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            course=course,
            phone_number=phone_number,
        )

        # Define senha e salvamento do usuário
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Cria um superusuário
    def create_superuser(self, email, full_name, course, phone_number, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            course=course,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Modelo de Usuário
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, error_messages={'unique': 'Um usuário com este nome já existe.'})
    email = models.EmailField(max_length=255, unique=True, error_messages={'unique': 'Um usuário com este e-mail já existe.'})
    phone_number = PhoneNumberField(null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, blank=True, upload_to="static/images/")

    # Define o gerenciador personalizado
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'course', 'phone_number']

    def __str__(self):
        return self.full_name
