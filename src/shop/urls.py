from django.urls import path
from shop import views

app_name = 'shop'


urlpatterns = [
    path('', views.index, name='initial_page'),
    path('homepage/', views.homepage_view, name="homepage"),
    path('products/', views.products_list, name='product_list')
]
