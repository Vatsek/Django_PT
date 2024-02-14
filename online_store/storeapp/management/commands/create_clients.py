from django.core.management.base import BaseCommand
from ...models import Client
from django.utils import lorem_ipsum
from random import randint, choice


class Command(BaseCommand):
    help = 'create clients'

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(
            name = f'Client {i}',
            email = f'client{i}@gmail.com',
            phone = phone_generate(),
            address = ''.join(lorem_ipsum.words(5, common=False))
            )
            client.save()
            self.stdout.write(f'Add {client.name}')


def phone_generate():
    code_phone = choice(['926', '915', '903'])
    number_phone = f'{randint(0, 9999999):07d}'
    return f'+7-{code_phone}-{number_phone}'