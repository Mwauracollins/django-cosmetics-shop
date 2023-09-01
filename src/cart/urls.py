from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.view_cart, name="view_cart"),
    path('delete-from-cart/<int:cart_item_id>/', views.delete_cart_items, name="delete_from_cart"),
]