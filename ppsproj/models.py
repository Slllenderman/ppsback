from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Provider(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="./static/logos", default=None) 
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="./static/prods", default=None)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

class ShoppingCart(models.Model):
    address = models.CharField(max_length=100)
    date = models.DateField()
    state = models.CharField(max_length=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    shCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)



