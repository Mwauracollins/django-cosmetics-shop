from django.db import models
from shop.models import Product
from accounts.models import Profile


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        
        
class Order(models.Model):
    order_items = models.ManyToManyField(OrderItem)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=100)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner} {self.ref_code}"

    def get_order_items(self):
        return self.items.all()

    def get_order_total(self):
        return sum([item.product.price for item in self.items.all()])

    class Meta:
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'