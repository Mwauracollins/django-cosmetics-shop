from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from cart.cart import CartObject
from shop.compare import Comparison
from shop.models import Category, Product, Wishlist


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


@login_required(login_url="accounts:login_page")
def index(request):
    products = Product.objects.all()
    context = {
        'products': paginat(request, products)
    }
    return render(request, 'shop/main.html', context)

@login_required(login_url="accounts:login_page")
def homepage_view(request):
    return render(request, "shop/index.html")


def products_list(request):
    return render(request, 'shop/product_list.html')


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
        # 'wishlist': 'wishlist',
        'related_products': related_products
    }
    # if request.user.wishlist.filter(id=product.id).first():
    #     context['wishlist'] = 'remove'

    return render(request, 'shop/product_detail.html', context)


def filter_by_category(request, slug):
    result = []
    category = Category.objects.filter(slug=slug).first()

    [
        result.append(product) \
        for product in Product.objects.filter(category=category.id).all()
    ]

    context = {
        'products': paginat(request, result)
    }
    return render(request, 'home')


@login_required(login_url='accounts:login_page')
def add_to_wishlist(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.get_or_create(user=user, product=product)

    return redirect('shop:wishlist')


@login_required(login_url='accounts:login_page')
def remove_from_wishlist(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.filter(user=user, product=product)
    wishlist.delete()

    return redirect('shop:wishlist')


@login_required(login_url='accounts:login_page')
def wishlist(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist': wishlist
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
    return render(request, 'shop/compare.html')

def add_to_compare(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    comparison = Comparison(request)
    comparison.add(product=product)
    comparison.save()

    return redirect('shop:compare')


def remove_from_compare(request, product_id):
    comparison = Comparison(request)
    product = get_object_or_404(Product, id=product_id)

    comparison.remove(product)
    comparison.save()

    return redirect('shop:compare')


def clear_compare(request):
    comparison = Comparison(request)
    comparison.clear()
    return redirect('shop:homepage')
