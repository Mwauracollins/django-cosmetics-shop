from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('blog-detail/', views.blog_detail, name="blog_detail")
]
