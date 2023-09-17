from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from cart.cart import CartObject
from orders.models import Order

from django_daraja.mpesa.core import MpesaClient


@login_required(login_url='login_page')
def checkout(request):
    user = request.user
    last_order = Order.objects.filter(owner=user).aggregate(Max('created_at'))['created_at__max']
    if last_order is not None:
        order = Order.objects.get(owner=user, created_at=last_order)
        cl = MpesaClient()

        phone_number = str(order.phone_number)
        amount = int(order.total_price)
        account_reference = 'CompanyXLTD'
        transaction_desc = 'Payment of X'
        callback_url = 'https://mydomain.com/path'
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        return HttpResponse(r)


def success(request):
    data = request.body
    return HttpResponse("Success webhook")


def failed(request):
    return HttpResponse("Failed WebHook")
