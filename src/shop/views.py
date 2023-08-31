from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Initial Page")


def products_list(request):
    return HttpResponse("Product List PASGE")


def product_detail(request):
    return HttpResponse("Product Detail")
