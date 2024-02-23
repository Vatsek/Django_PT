from django.urls import path
from . import views
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', index, name='index'),
    path('client/orders/<int:client_id>/', views.get_orders_by_client_id, name='get_orders'),
    path('client/products/<int:client_id>/', views.get_client_purchased_products, name='get_client_purchased_products'),
    path('products/new_product/', views.new_product, name='add_product_form'),
    path('products/product/<int:product_id>', views.get_product_by_id, name='get_product_by_id'),
    path('products/product_update_form/<int:product_id>', views.product_update_form, name='product_update_form')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
