from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    length = models.DecimalField(max_digits=8, decimal_places=2, help_text="length in centimeter(cm)")
    width = models.DecimalField(max_digits=8, decimal_places=2, help_text="width in centimeters(cm)")
    height = models.DecimalField(max_digits=8, decimal_places=2, help_text="height in centimeter(cm)")
    weight = models.DecimalField(max_digits=8, decimal_places=3, help_text="weigth in kilogram(kg)")

    def __str__(self):
        return self.name

class ShippingBox(models.Model):
    name = models.CharField(max_length=80)
    length = models.DecimalField(max_digits=8, decimal_places=2, help_text="length in centimeter(cm)")
    width = models.DecimalField(max_digits=8, decimal_places=2, help_text="width in centimeter(cm)")
    height = models.DecimalField(max_digits=8, decimal_places=2, help_text="height in centimeter(cm)")
    max_weight = models.DecimalField(max_digits=8, decimal_places=3, help_text="weight in kilogram(kg)")
    cost = models.DecimalField(max_digits=8, decimal_places=2, help_text="cost in rupees(Rs)")

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} * {self.quantity}"