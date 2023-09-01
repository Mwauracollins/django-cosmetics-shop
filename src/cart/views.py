from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from accounts.models import Profile
from cart.models import Cart, CartItem
from shop.models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(owner=request.user.profile)

    cart_item, item_created = CartItem.object.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.cart_item_quantity += 1
        cart_item.save()
    return redirect('view_cart')


def view_cart(request):
    cart = Cart.objects.all(owner=request.user.profile)
    cart_items = cart.get_cart_items()
    cart_total = cart.get_cart_total()
    
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    
    return render(request, 'cart/cart.html', context)


def delete_cart_items(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, cart_owner=request.user.profile)
    
    if cart_item.cart_item_quantity > 1:
        cart_item.cart_item_quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
        
    return redirect('view_cart')