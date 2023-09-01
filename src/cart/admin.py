from django.contrib import admin
from cart.models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_atfi')

admin.site.register(Cart, CartAdmin)

class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']
