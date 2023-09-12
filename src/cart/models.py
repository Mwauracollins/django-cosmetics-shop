from django.contrib.sessions.models import Session

from django.db import models
from shop.models import Product
from accounts.models import Profile
from django.utils import timezone

        
class Cart(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    session_key = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.owner
    def get_cart_items(self):
        return self.items.all()
    def get_cart_total(self):
        total_cost = sum(item.get_cost() or 0 for item in self.get_cart_items())
        return total_cost
    
    class Meta:
        db_table = 'Cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    cart_item_quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    
    def get_cost(self):
        self.product.price * self.cart_item_quantity

    class Meta:
        db_table = 'CartItem'
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'
        