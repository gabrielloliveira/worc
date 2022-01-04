from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from worc.apps.core.models import BaseModel
from worc.apps.users.managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    Overwrite default User model.
    """

    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=500)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
