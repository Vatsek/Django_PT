from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['date_product_add']
        labels = {'title': 'Наименование',
                  'description': 'Описание',
                  'price': 'Стоимость',
                  'quantity_of_product': 'количество',
                  'image': 'Изображение'}

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
