from datetime import timedelta, date

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import Order, Product
from .forms import ProductForm


def index(request):
    return render(request, 'storeapp/index.html')


def get_orders_by_client_id(request, client_id):
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


def new_product(request):
    title = 'Добавление товара'
    input_value = 'Добавить'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product_form')
    else:
        form = ProductForm()
    return render(request, 'storeapp/product_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value})


def product_update_form(request, product_id):
    title = 'Обновление товара'
    input_value = 'Обновить'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.get(pk=product_id)
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity_of_product = form.cleaned_data['quantity_of_product']
            product.image = form.cleaned_data['image']
            product.save()
            return redirect('product_update_form', product_id)
    else:
        form = ProductForm(instance=Product.objects.get(pk=product_id))
    return render(request, 'storeapp/product_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value})


def get_product_by_id(request, product_id):
    product = Product.objects.get(pk=product_id)
    title = 'Товар'
    return render(request, 'storeapp/product.html', {'product': [product], 'title': title})
