from django.shortcuts import render
from django.http import HttpResponse


def get_pending_orders(request):
    return HttpResponse("Pending Orders")
