from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from cart.cart import CartObject
from orders.models import Order, OrderItem


def create_order(request):
    cart = CartObject(request)
    order = Order.objects.create(owner=request.user)
    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            price=item['price'],
            order_item_quantity=item['quantity']
        )
    cart.clear()

    return redirect(reverse('payment:checkout'))



def get_pending_orders(request):
    return HttpResponse("Pending Orders")


def order_details(request):
    return HttpResponse("Order History")


def delete_from_cart(request):
    return HttpResponse("Deletes from order list")
