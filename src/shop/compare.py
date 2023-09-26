import requests
from django.conf import settings
from shop.models import Product


class Compare:
    def __init__(self):
        self.session = requests.session
        self.comparison = self.add_compare_session()
        self.product_ids = self.get_product_ids

    def add_compare_session(self):
        comparison = self.session.get(settings.COMPARISON_SESSION_ID)
        if not comparison:
            comparison = self.session[settings.COMPARISON_SESSION_ID] = {}
        return comparison

    def add(self, product):
        product_id = str(product.id)

        if product_id not in self.comparison:
            self.comparison[product_id] = {
                'product_name': product.name,
                'price': str(product.price)
            }
            self.save()
    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.comparison:
            del self.comparison[product_id]
            self.save()

    def __iter__(self):
        products = Product.objects.filter(id__in=self.comparison.keys())
        for product in products:
            self.comparison[str(product.id)]['product'] = product

        for item in self.comparison.values():
            yield item

    def get_product_ids(self):
        return [product_id for product_id in self.comparison.keys()]

    def clear(self):
        del self.session[settings.COMPARISON_SESSION_ID]
        self.save()

    def save(self):
        self.session[settings.COMPARISON_SESSION_ID] = self.comparison
        self.session.modified = True
