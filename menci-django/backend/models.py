from django.db import models
from datetime import datetime

class Image(models.Model):
    src = models.ImageField(upload_to='static/assets')
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    description = models.CharField(max_length=1000)
    images = models.ManyToManyField(Image)
    sold_out = models.BooleanField(default=False)

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    city = models.CharField(max_length=10)

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    price = models.PositiveBigIntegerField(default=0)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()

class Subscriber(models.Model):
    email = models.EmailField()

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

class Message(models.Model):
    sender_first_name = models.CharField(max_length=1000, default='')
    sender_last_name = models.CharField(max_length=1000, default='')
    content = models.TextField(max_length=10000)