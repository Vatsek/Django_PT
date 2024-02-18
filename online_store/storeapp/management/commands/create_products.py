import decimal

from django.core.management.base import BaseCommand
from ...models import Product
import random


class Command(BaseCommand):
    help = 'create products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count+1):
            product = Product(
            title = f'Product {i}',
            description = f'Description product {i}',
            price = decimal.Decimal(random.randrange(10000))/100,
            quantity_of_product = random.randint(1, 30)
            )
            product.save()
            self.stdout.write(f'Add {product.title}')

