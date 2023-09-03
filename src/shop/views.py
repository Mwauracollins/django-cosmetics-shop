from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator
from shop.forms import QuantityForm

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
    html = '<a href="{% url "accounts:logout_user"%}">logout</a>'
    context = {
        'html': html
    }
    return HttpResponse(context)


def products_list(request):
    return HttpResponse("Product List PASGE")


def product_detail(request, slug):
    form = QuantityForm()
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).all()[:5]
    context = {
		'name':product.name,
		'product':product,
		'form':form,
		'related_products':related_products
	}
    return render(request, 'shop/product_detail.html', context)

def filter_by_category(request, slug):
	"""when user clicks on parent category
	we want to show all products in its sub-categories too
	"""
	result = []
	category = Category.objects.filter(slug=slug).first()
	[result.append(product) \
		for product in Product.objects.filter(category=category.id).all()]
	# check if category is parent then get all sub-categories
	context = {'products': paginat(request ,result)}
	return render(request, 'home_page.html', context)
