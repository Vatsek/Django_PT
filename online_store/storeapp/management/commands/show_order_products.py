from django.core.management.base import BaseCommand
from ...models import Order



class Command(BaseCommand):
    help = 'Show order products'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            print(order.products.all())
        else:
            self.stdout.write(f'There is no order with this id')
