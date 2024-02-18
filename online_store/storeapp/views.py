from datetime import timedelta, date

from django.shortcuts import render
from .models import Order


def index(request):
    return render(request, 'storeapp/index.html')


def get_orders_by_id(request, client_id):
    orders = Order.objects.filter(client_id=client_id)
    context = []
    for order in orders:
        products = order.products.all()
        context.append({'order': order, 'products': products})
    return render(request, 'storeapp/orders.html', {'orders': context})


def get_client_purchased_products(request, client_id):
    def get_product_from_order(orders):
            products_lst = []
            if orders:
                for order in orders:
                    products = order.get_products()
                    for product in products:
                        products_lst.append(product)
            else:
                products_lst.append('Заказы отсутствуют')
            return set(products_lst)

    last_week_orders = Order.objects.filter(client=client_id, date_order__gte=date.today() - timedelta(days=7))
    last_month_orders = Order.objects.filter(client=client_id, date_order__gte=date.today() - timedelta(days=30))
    last_year_orders = Order.objects.filter(client=client_id, date_order__gte=date.today() - timedelta(days=365))

    last_week_products = get_product_from_order(last_week_orders)
    last_month_products = get_product_from_order(last_month_orders)
    last_year_products = get_product_from_order(last_year_orders)

    return render(request, 'storeapp/client_purchased_products.html',
                  {'week_prod': last_week_products,
                            'month_prod': last_month_products,
                            'year_prod': last_year_products})
