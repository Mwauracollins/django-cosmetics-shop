from django.contrib import admin

from shop.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['display_categories', 'name', 'price', 'stock_quantity', 'product_image']
    list_filter = ['category', 'price']
    search_fields = ['name']

    def display_categories(self, obj):
        return ",".join([category.name for category in obj.category.all()])

    display_categories.short_description = 'Categories'


admin.site.register(Product, ProductAdmin)
