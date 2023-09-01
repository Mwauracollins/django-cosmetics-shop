from django.db import models
from shop.models import Product
from accounts.models import Profile


class Order(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=100)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner} {self.ref_code}"

    def get_order_items(self):
        return self.items.all()

    def get_order_total(self):
        total_cost = sum(item.get_cost() for item in self.get_order_items())
        return total_cost
    
    class Meta:
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order_item = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='items')
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    order_item_quantity = models.PositiveIntegerField(default=1, null=True )
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

    def get_cost(self):
        return self.product.price * self.order_item_quantity

    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        
        
