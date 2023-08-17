from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:id>', views.index_id, name='product'),
    path('cart', views.index, name='cart'),
    path('contact', views.index, name='contact'),
    path('productList', views.index, name='productList'),
    path('validation', views.index, name='validation'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''path('products', views.products, name='products'),
    path('product/<str:id>', views.product, name='product'),
    path('bag', views.bag, name='bag'),
    path('remove_item/<str:id>', views.remove_item, name='remove_item'),
    path('order', views.order, name='order'),
    path('validated', views.validated, name='validated'),
    path('contact', views.contact, name='contact'),'''