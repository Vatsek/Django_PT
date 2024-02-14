from django.core.management.base import BaseCommand
from ...models import Product, Order
from random import choice


class Command(BaseCommand):
    help = 'add product to order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            product = choice(Product.objects.all())
            order.products.add(product)
            order.total_amount += product.price
            order.save()
            self.stdout.write(f'Product {product.title} add to order {order.pk}')
        else:
            self.stdout.write(f'There is no order with this id')

