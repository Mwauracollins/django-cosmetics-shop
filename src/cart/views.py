from django.shortcuts import render
from django.http import HttpResponse


def add_to_cart(request):
    return HttpResponse()


def view_cart(request):
    return HttpResponse("View the cart items")

def delete_cart_items(request):
    return HttpResponse("Delete cart items")
