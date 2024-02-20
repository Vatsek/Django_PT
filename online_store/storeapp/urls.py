from django.urls import path
from . import views
from .views import index, product_update_form


urlpatterns = [
    path('index/', index, name='index'),
    path('orders/<int:client_id>/', views.get_orders_by_id, name='get_orders'),
    path('products/<int:client_id>/', views.get_client_purchased_products, name='get_client_purchased_products'),
    path('products/product_update_form/<int:product_id>', views.product_update_form, name='product_update_form'),
]
