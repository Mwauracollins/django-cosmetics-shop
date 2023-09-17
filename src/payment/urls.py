from django.urls import path
from payment import views

app_name = "payment"


urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('success/', views.success, name="success"),
    path('failed/', views.failed, name='failed')
]
