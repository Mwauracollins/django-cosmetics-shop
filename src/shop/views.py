from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Initial Page")


def homepage_view(request):
    html = '<a href="{% url "accounts:logout_user"%}">logout</a>'
    context ={
        'html': html
    }
    return HttpResponse(context)


def products_list(request):
    return HttpResponse("Product List PASGE")


def product_detail(request):
    return HttpResponse("Product Detail")
