from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(Provider)
