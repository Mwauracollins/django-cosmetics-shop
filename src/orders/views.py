from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
        order, created = Order.objects.create(owner=user), None
        cart = Cart.objects.get(owner=user)
        if order:
            order.first_name = request.POST.get('first_name')
            order.last_name = request.POST.get("last_name")
            order.tracking_number = generate_tracking_number()
            order.email = request.POST.get("email")
            order.phone_number = +254748463235
            order.address = request.POST.get("address")
            order.region = request.POST.get("region")
            order.town = request.POST.get("town")
            order.payment_method = request.POST.get("payment_method")
            order.save()

            order.total_price = cart.get_total_price()
            order.save()

        cart_items = CartItem.objects.filter(cart=cart)
        print("Cart item called")

        print("Order item called")
        for item in cart_items:
            order_item = OrderItem.objects.create(order=order)
            order_item.product = item.product
            order_item.price = item.product.price
            order_item.order_item_quantity = item.quantity
            print(" item data called")

            order_item.save()
            cart_items.delete()

        messages.success(request, "Order created successfully")
        print("Sava")
        return redirect('payment:checkout')
    return render(request, 'orders/create_order.html')

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
