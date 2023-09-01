from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.http import HttpResponse


def profile_details(request):
    return HttpResponse("Profile Details")


def login_view(request):
    login()
    authenticate()
    return HttpResponse("Login Page")


def signup_view(request):
    return HttpResponse("SignUp Page")


def logout_user(request):
    logout(request)
