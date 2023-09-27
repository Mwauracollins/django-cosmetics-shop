from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.forms import RegistrationForm
from accounts.models import Profile


@login_required(login_url='accounts:login_page')
def profile_details(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:homepage')
        else:
            messages.info(request, "Username or Password is incorrect")
    return render(request, "accounts/login.html")


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = Profile()
            user.first_name = first_name
            user.last_name = last_name
            user.username = email
            user.email = email
            user.phone_number = phone_number
            user.set_password(password)
            user.save()

            return redirect('shop:homepage')
        else:
            error_message = messages.error("Passwords do not match")
            context = {
                'error_message': error_message
            }
            return render(request, 'accounts/signup.html', context)

    return render(request, 'accounts/signup.html')


def logout_user(request):
    logout(request)
    return redirect('accounts:login_page')
