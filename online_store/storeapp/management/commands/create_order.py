import decimal

from django.core.management.base import BaseCommand
from ...models import Client, Order
from random import choice


class Command(BaseCommand):
    help = 'create order'

    def handle(self, *args, **kwargs):
        client = choice(Client.objects.all())
        order = Order(
            client = client,
            total_amount = decimal.Decimal(0),
        )
        order.save()
        self.stdout.write(f'Order created')
