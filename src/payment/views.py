from django.shortcuts import render
from django.http import HttpResponse


def checkout(request):
    return HttpResponse("Cheout Page")


def success(request):
    return HttpResponse("Success webhook")


def failed(request):
    return HttpResponse("Failed WebHook")
