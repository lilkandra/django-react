from django.contrib import admin
from .models import Product, Client, Item, Order, Message, Subscriber

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Message)
admin.site.register(Subscriber)