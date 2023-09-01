from django.urls import path
from accounts import views

app_name = "accounts"


urlpatterns = [
    path('profile/', views.profile_details, name="profile_details"),
    path('login/', views.login_view, name='login_page'),
    path('signup/', views.signup_view, name="signup_page"),
    path('logout/', views.logout_user, name="logout_user")
]
