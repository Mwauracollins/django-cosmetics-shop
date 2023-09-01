from django.shortcuts import render
from django.http import HttpResponse


def get_pending_orders(request):
    return HttpResponse("Pending Orders")


def order_details(request):
    return HttpResponse("Order History")


def delete_from_cart(request):
    return HttpResponse("Deletes from order list")
