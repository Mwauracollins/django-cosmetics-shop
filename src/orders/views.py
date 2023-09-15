from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from cart.cart import CartObject
from cart.models import Cart, CartItem
from orders.extra import generate_tracking_number
from orders.models import Order, OrderItem
from shop.models import Product


@login_required(login_url='accounts:login_page')
def create_order(request):
    user = request.user
    if request.method == 'POST':
        order, created = Order.objects.create(owner=user)
        order.


            # product = get_object_or_404(Product, id=cart_item['product'].id)
            # if product.stock_quantity >= cart_item['quantity']:
            #     product.stock_quantity -= cart_item['quantity']
            #     product.save()
            # else:
            #     messages.info("Product out of stock")


def get_pending_orders(request):
    return HttpResponse("Pending Orders")


def order_details(request):
    return HttpResponse("Order History")


def delete_from_cart(request):
    return HttpResponse("Deletes from order list")
