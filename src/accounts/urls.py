from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile_details, name="profile_details"),
    path('login/', views.login_view, name='login_page'),
    path('signup/', views.signup_view, name="signup_page"),
]