from django.urls import path
from . import views


urlpatterns = [
    path('getProducts', views.getProducts, name='products_api'),
    path('getProduct/<str:id>', views.getProduct, name='getProduct_byId'),
    path('validateBag', views.validateBag, name='validateBag_api'),
]