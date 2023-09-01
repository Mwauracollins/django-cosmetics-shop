from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    username = models.CharField(unique=True, null=True, max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phone_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    USERNAME_FIELD = 'username'
