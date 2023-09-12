from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from cart.cart import CartObject
from shop.models import Category, Product


def paginat(request, list_objects):
    p = Paginator(list_objects, 20)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj


def index(request):
    products = Product.objects.all()
    context = {
        'products': paginat(request, products)
    }
    return render(request, 'shop/main.html', context)


def homepage_view(request):
    return render(request, "shop/index.html")


def products_list(request):
    return HttpResponse("Product List PASGE")


@login_required(login_url='accounts:login_page')
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        cart = CartObject(request)
        quantity = int(request.POST.get('quantity', 0))
        cart.add(product=product, quantity=quantity)
        return redirect('cart:view_cart')

    related_products = Product.objects.filter(category=product.category).all()[:5]
    context = {
        'product': product,
        'wishlist': 'wishlist',
        'related_products': related_products
    }
    if request.user.wishlist.filter(id=product.id).first():
        context['wishlist'] = 'remove'

    return render(request, 'shop/product_detail.html', context)


def filter_by_category(request, slug):
    result = []
    category = Category.objects.filter(slug=slug).first()

    [
        result.append(product) \
 \
        for product in Product.objects.filter(category=category.id).all()
    ]

    context = {
        'products': paginat(request, result)
    }
    return render(request, 'home')


@login_required(login_url='accounts:login_page')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.wishlist.add(product)

    return redirect('shop:wishlist',
                    # slug=product.slug
                    )


@login_required(login_url='accounts:login_page')
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.wishlist.remove(product)

    return redirect('shop:wishlist')


@login_required(login_url='accounts:login_page')
def wishlist(request):
    products = request.user.wishlist.all()
    context = {
        'title': 'Wishlist',
        'products': products
    }
    return render(request, 'shop/wishlist.html', context)


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query).all()

    context = {
        'products': paginat(request, products)
    }
    return render(request, 'homepage.html', context)


def about(request):
    return HttpResponse("About Us")


def contact(request):
    return render(request, "shop/contact-us.html")


def compare(request):
    return HttpResponse("compare")
