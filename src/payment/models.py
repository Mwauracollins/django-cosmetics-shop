from django.db import models

from accounts.models import Profile
from orders.models import Order


class Transaction(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.ref_code} {self.order.get_order_total()}"

    class Meta:
        db_table = 'Transaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'