from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='initial_page'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('homepage/', views.homepage_view, name="homepage"),
    path('products/', views.products_list, name='product_list'),
    path('filter/<slug:slug>/', views.filter_by_category, name="filter_by_category"),
    path('about/', views.about, name="about"),
    path('add/wishlist/<int:product_id>/', views.add_to_wishlist, name="add_to_wishlist"),
    path('remove/wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('about/', views.about, name="about"),
    path('compare/', views.compare, name="compare"),
    path('contact/', views.contact, name="contact"),
    path('add-to-compare/<int:product_id>/', views.add_to_compare, name="add_to_compare"),
    path('remove_from_compare/<int:product_id>/', views.remove_from_compare, name="remove_from_compare"),
    path('clear_compare/', views.clear_compare, name="clear_compare")
]
