from django.urls import path
from orders import views

app_name = "orders"


urlpatterns = [
    path('pending-orders/', views.get_pending_orders, name="pending_orders"),
    path('create-order/', views.create_order, name="create_order")
]
