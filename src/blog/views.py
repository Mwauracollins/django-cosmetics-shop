from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    return render(request, "blog/blog.html")


def blog_detail(request):
    return render(request, 'blog/blog_detail.html')
