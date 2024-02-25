from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity_of_product=0)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'date_of_reg']
    list_filter = ['date_of_reg']
    readonly_fields = ['date_of_reg']
    fieldsets = ((None, {'fields': ['name', 'date_of_reg']}),
                 ('Контакты', {'fields': ['email', 'phone', 'address']}))
    search_fields = ['phone', 'email']
    search_help_text = 'Поиск по номеру телефона или почте'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity_of_product', 'date_product_add', 'image']
    list_filter = ['price', 'quantity_of_product', 'date_product_add']
    readonly_fields = ['date_product_add']
    fieldsets = (('Информация о товаре', {'fields': ['title', 'description', 'date_product_add']}),
                 ('Склад и финансы', {'fields': ['quantity_of_product', 'price']}),
                 ('Изображение', {'fields': ['image']}),)
    actions = [reset_quantity]
    search_fields = ['description', 'title']
    search_help_text = 'Поиск по названию или описанию'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'total_amount', 'date_order']
    list_filter = ['date_order']
    readonly_fields = ['date_order']
    fieldsets = (('Информация о заказе', {'fields': ['client', 'total_amount', 'date_order']}),
                 ('Продукты', {'fields': ['products']}),)
    filter_horizontal = ['products']

