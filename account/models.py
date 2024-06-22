from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import  gettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username,password=None, **extra_fields):
        if not email:
            raise ValueError("Email field must be set")
        email =self.normalize_email(email)
        user =self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser =True")
        
        return self.create_user(email, username, password, **extra_fields)
    
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=70)
    username = models.CharField( _("username"), max_length=60, unique=True)
    is_staff = models.BooleanField(_("is staff"), default=False)

    object =CustomUserManager()

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS =["username"]

    def __str__(self) -> str:
        return self.email


        


