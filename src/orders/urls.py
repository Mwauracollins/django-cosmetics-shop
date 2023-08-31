from django.urls import path
from . import views

urlpatterns = [
    path('pending-orders/', views.get_pending_orders, name="pending_orders")
]