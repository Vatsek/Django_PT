# Generated by Django 5.0.2 on 2024-02-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products', to='storeapp.product'),
        ),
    ]