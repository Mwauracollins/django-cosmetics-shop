from django.db import models
from shop.models import Product
from accounts.models import Profile

        
class Cart(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_item_quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = 'CartItems'
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'
        