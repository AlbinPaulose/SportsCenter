from django.db import models
from django.contrib.auth.models import User
from Index.models import *
from django.conf import settings

# Create your models here.
order_status = (
    ("not paid", "not paid"),
    ("payment confirmed", "payment confirmed")
)


class CartTable(models.Model):
    user_id = models.IntegerField(blank=False)
    product_id = models.ForeignKey(ProductsDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = self.quantity * self.product_id.product_selling_price
        return total


class WishlistTable(models.Model):
    user_id = models.IntegerField(blank=False)
    product_id = models.ForeignKey(ProductsDetails, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class OrderTable(models.Model):
    orderId = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    subtotal = models.IntegerField()
    status = models.CharField(default='not paid', choices=order_status,max_length=100)
