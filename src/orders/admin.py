from django.contrib import admin
from orders.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'is_ordered']


admin.site.register(Order, OrderAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
