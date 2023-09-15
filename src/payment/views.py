from django.shortcuts import render
from django.http import HttpResponse

from cart.cart import CartObject
from orders.models import Order


def checkout(request):
    user = request.user
    order = Order.objects.create(owner=user)
    cart = CartObject(request).cart


    return render(request, "payment/checkout.html")


def success(request):
    return HttpResponse("Success webhook")


def failed(request):
    return HttpResponse("Failed WebHook")
