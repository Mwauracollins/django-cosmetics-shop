from django.urls import path
from shop import views

app_name = 'shop'


urlpatterns = [
    path('', views.index, name='initial_page'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('homepage/', views.homepage_view, name="homepage"),
    path('products/', views.products_list, name='product_list'),
    path('filter/<slug:slug>/', views.filter_by_category, name="filter_by_category")
]
