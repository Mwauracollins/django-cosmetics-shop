from cart.cart import CartObject


def cart(request):
    return {
        'cart': CartObject(request)
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
