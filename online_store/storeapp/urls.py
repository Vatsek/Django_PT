from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path('index/', index, name='index'),
    path('orders/<int:client_id>/', views.get_orders_by_id, name='get_orders'),
    path('products/<int:client_id>/', views.get_client_purchased_products, name='get_client_purchased_products'),
]
