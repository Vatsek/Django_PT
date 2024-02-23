from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Имя')
    email = models.EmailField(verbose_name=u'Почта')
    phone = models.CharField(max_length=12, verbose_name=u'Телефон')
    address = models.CharField(max_length=200, verbose_name=u'Адрес')
    date_of_reg = models.DateField(auto_now_add=True, verbose_name=u'Дата регистрации')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=u'Цена')
    quantity_of_product = models.IntegerField(verbose_name=u'Доступно товара')
    date_product_add = models.DateField(auto_now_add=True, verbose_name=u'Дата добавления товара')
    image = models.ImageField(upload_to='images', blank=True, verbose_name=u'Изображение')

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=u'Клиент')
    products = models.ManyToManyField('Product', verbose_name=u'Продукты')
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=u'Сумма заказа')
    date_order = models.DateField(auto_now_add=True, verbose_name=u'Дата заказа')


    def __str__(self):
        return f'Заказ № {self.pk}'

    def get_products(self):
        return self.products.all()
