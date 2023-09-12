from django.conf import settings
from decimal import Decimal

from cart.models import Cart, CartItem
from shop.models import Product


class CartObject:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.add_cart_session()
        self.product_ids = self.get_product_ids()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = Decimal(item['price']) * int(item['quantity'])
            yield item

    # Make a new cart session if there was none
    def add_cart_session(self):
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        return cart

    def get_or_create_cart(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(owner=request.user)
            return cart
        return None

    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
            self.cart[product_id]['quantity'] = quantity

        self.cart.get(product_id)['quantity'] = quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    # Total quantity of items
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_product_ids(self):
        return [product_id for product_id in self.cart.keys()]

    def get_total_distinct_items(self):
        return len(self.product_ids)

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
