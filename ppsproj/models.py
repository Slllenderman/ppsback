from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from datetime import datetime


class Provider(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="./static/logos", blank=True) 
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    STATES = [
        ('S', 'Sellable'),
        ('D', 'Deleted')
    ]
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=1, choices=STATES, default='S')
    price = models.FloatField()
    category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="./static/prods", blank=True)
    description = models.CharField(max_length=1000)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
 
class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    STATES = [
        ('A', 'Processing'),
        ('B', 'WaitingPayment'),
        ('C', 'Confirmed'),
        ('D', 'Rejected')
    ]
    address = models.CharField(max_length=100)
    date = models.DateField()
    creatingTime = models.DateField(default=datetime.now().date())
    confirmedTime = models.DateField(null=True)
    state = models.CharField(max_length=1, choices=STATES, default='A')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    STATES = [
        ('P', 'Processing'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    state = models.CharField(max_length=1, choices=STATES, default='P')
    shCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)


