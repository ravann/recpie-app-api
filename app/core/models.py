from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, nickname=None, **extra_fields):
        """Creates and saves a new user"""
        if (email is None):
            raise ValueError("Must provide email!!!")
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, nickname=None):
        """Creates and saves a new user"""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustUser(AbstractBaseUser, PermissionsMixin):
    """Customer user supports email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    nickname = models.CharField(max_length=255, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
