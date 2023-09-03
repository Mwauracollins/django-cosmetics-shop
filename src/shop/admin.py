from django.contrib import admin

from shop.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price', 'stock_quantity', 'image']
    list_filter = ['category', 'price']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
