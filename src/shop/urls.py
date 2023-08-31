from django.urls import path
from shop import views


urlpatterns = [
    path('', views.index, name='initial_page'),
    path('products/', views.products_list, name='product_list')
]
