from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order
from django.http import HttpResponse


def index(request):
    return render(request, 'storeapp/index.html')


def get_orders_by_id(request, client_id):
    orders = Order.objects.filter(client_id=client_id)
    context = []
    for order in orders:
        products = order.products.all()
        context.append({'order': order, 'products': products})
    return render(request, 'storeapp/orders.html', {'orders': context})
