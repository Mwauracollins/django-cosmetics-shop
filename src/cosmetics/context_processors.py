from cart.cart import CartObject
from cart.models import Cart
from shop.compare import Comparison
from shop.models import Wishlist


def cart(request):
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.get(owner=user)
        return {
            'cart': cart.get_cart_items(),
            'get_total_distinct_items': cart.get_total_dictinct_items(),
            'get_total_price': cart.get_total_price(),
        }
    else:
        cart = CartObject(request)
        return {
            'cart': cart,
            'get_total_distinct_items': cart.get_total_distinct_items(),
            'get_total_price': cart.get_total_price()
        }


def user_info(request):
    user = {}
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    return {
        'user': user
    }

def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)

    return {
        'wishlist': wishlist
    }
    

def comparison(request):
    compare = Comparison(request)
    return {
        'compare' : compare

    }
