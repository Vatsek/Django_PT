import decimal

from django.core.management.base import BaseCommand
from ...models import Client, Order, Product
from random import choice


class Command(BaseCommand):
    help = 'create order'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('count', type=int, help='count of products')

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('client_id')
        count = kwargs.get('count')
        client = Client.objects.filter(pk=client_id).first()
        order = Order(
            client = client,
            total_amount = decimal.Decimal(0),
        )
        order.save()
        for _ in range(count):
            product = choice(Product.objects.all())
            order.products.add(product)
            order.total_amount += product.price
            order.save()
        self.stdout.write(f'Order created')

