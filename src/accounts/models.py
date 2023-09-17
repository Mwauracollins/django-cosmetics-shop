from django.db import models
from django.contrib.auth.models import AbstractUser

from shop.models import Product


class Profile(AbstractUser):
    username = models.CharField(unique=True, null=True, max_length=200)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.email
    
    def get_wishlist_count(self):
        return self.wishlist.count()

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    USERNAME_FIELD = 'username'
