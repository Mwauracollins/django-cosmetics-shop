from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

from accounts.forms import RegistrationForm


def profile_details(request):
    return HttpResponse("Profile Details")


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
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            form.save()

            return redirect('shop:homepage')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)


def logout_user(request):
    logout(request)
