from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from cart.cart import CartObject
from cart.models import CartItem, Cart
from shop.models import Product


@login_required(login_url='accounts:login_page')
# @require_POST
def add_to_cart(request, product_id):
    user = request.user
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart = CartObject(request)
        quantity = int(request.POST.get('quantity', 0))
        cart.add(product=product, quantity=quantity)
        
        if user.is_authenticated:
            user_cart, created = Cart.objects.get_or_create(owner=request.user)

            cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
            cart_item.cart_item_quantity = quantity
            cart_item.save()
            user_cart.save()

            

    return redirect('cart:view_cart')


@login_required(login_url='accounts:login_page')
def view_cart(request):
    cart = CartObject(request)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(
    #         initial={
    #             'quantity': item['quantity'],
    #             'update': True
    #         }
    #     )

    return render(request, 'cart/cart.html')


@login_required(login_url='accounts:login_page')
def delete_cart_items(request, product_id):
    cart = CartObject(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, "Item removed from cart")
    return redirect('cart:view_cart')
