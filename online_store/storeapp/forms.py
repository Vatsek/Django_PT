from django import forms
from .models import Product


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['date_product_add']
        labels = {'title': 'Наименование',
                  'description': 'Описание',
                  'price': 'Стоимость',
                  'quantity_of_product': 'количество'}