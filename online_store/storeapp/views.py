from datetime import timedelta, date
from django.shortcuts import render, redirect
from .models import Order, Product
from .forms import ProductUpdateForm


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
            products_set = set()
            if orders:
                for order in orders:
                    products_set.update(order.get_products())
            else:
                products_set.add('Заказы отсутствуют')
            return products_set 

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


# def product_update_form(request):
#     if request.method == 'POST':
#         form = ProductUpdateForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             form = ProductUpdateForm(instance=Product.objects.first())
#             # Product.objects.create(title=data['title'],
#             #                         description=data['description'],
#             #                         price=data['price'],
#             #                         quantity_of_product=data['quantity_of_product'])
#             return redirect('product_update_form')
#     else:
#         form = ProductUpdateForm()
#     return render(request, 'storeapp/product_update_form.html', {'form': form})


def product_update_form(request, product_id):
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(pk=product_id)
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity_of_product = form.cleaned_data['quantity_of_product']
            product.save()
            return redirect('product_update_form', product_id)
    else:
        form = ProductUpdateForm(instance=Product.objects.get(pk=product_id))
    return render(request, 'storeapp/product_update_form.html', {'form': form})

