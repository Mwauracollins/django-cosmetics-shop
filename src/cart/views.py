from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from cart.cart import CartObject
from cart.models import CartItem, Cart
from shop.models import Product


# @login_required(login_url='accounts:login_page')
# @require_POST
def add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if request.method == "POST":
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(owner=user)

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
            )
            cart_item.quantity = quantity
            cart_item.save()
            cart.save()
        else:
            cart = CartObject(request)
            cart.add(product=product, quantity=quantity)

    return redirect('cart:view_cart')


# @login_required(login_url='accounts:login_page')
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


# @login_required(login_url='accounts:login_page')
def delete_cart_items(request, product_id):
    user = request.user

    if user.is_authenticated:
        cart = Cart.objects.get(owner=user)
        cart_item = CartItem.objects.filter(cart=cart)
        cart_item.delete()
    else:
        cart = CartObject(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        messages.success(request, "Item removed from cart")
    return redirect('cart:view_cart')
