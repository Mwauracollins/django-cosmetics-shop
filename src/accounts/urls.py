from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile_details, name="profile_details"),
]