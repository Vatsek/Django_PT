import decimal

from django.core.management.base import BaseCommand
from ...models import Product
import random


class Command(BaseCommand):
    help = 'create products'

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(
            title = f'Product {i}',
            description = f'Description product {i}',
            price = decimal.Decimal(random.randrange(10000))/100,
            quantity_of_product = random.randint(1, 30)
            )
            product.save()
            self.stdout.write(f'Add {product.title}')

