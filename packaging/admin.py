from django.contrib import admin

# Register your models here.
from .models import Product, ShippingBox, Order, OrderItem

admin.site.register(Product)
admin.site.register(ShippingBox)
admin.site.register(Order)
admin.site.register(OrderItem)