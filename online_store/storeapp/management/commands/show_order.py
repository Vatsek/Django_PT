from django.core.management.base import BaseCommand
from ...models import Product, Order


class Command(BaseCommand):
    help = 'show order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            products = Product.objects.filter(order=order)
            intro = f'All products in order:\n'
            text = '\n'.join(product.title for product in products)
            self.stdout.write(f'{intro}{text}')
        else:
            self.stdout.write(f'There is no order with this id')


