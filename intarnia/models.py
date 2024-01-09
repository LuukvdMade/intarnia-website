from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ProfileManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password=None, **other_fields):
        if not email:
            raise ValueError("not a valid email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class Profile(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]
    email = models.EmailField(("email adress"), unique = True)
    user_name = models.CharField(max_length = 150, unique = True)
    is_staff = models.BooleanField(default = False)
    is_superuser= models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

    objects = ProfileManager()

    def __str__(self):
        return self.user_name

