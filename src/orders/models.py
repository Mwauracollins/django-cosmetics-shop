from django.db import models
from shop.models import Product
from accounts.models import Profile


class Order(models.Model):
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Shipping', 'Shipping')
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tracking_number = models.CharField(max_length=100)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=2048, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=250, null=True)
    region = models.CharField(max_length=250, null=True)
    town = models.CharField(max_length=250, null=True)

    payment_method = models.CharField(max_length=250, null=True)
    payment_id = models.CharField(max_length=150, null=True)
    order_status = models.CharField(choices=ORDER_STATUS, max_length=150, null=True,default="Pending")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.owner} {self.tracking_number}"

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
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_item_quantity = models.PositiveIntegerField(default=1, null=True )
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.order.id

    def get_cost(self):
        return self.product.price * self.order_item_quantity

    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        
        
