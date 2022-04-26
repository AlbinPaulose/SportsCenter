from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(OrderTable)
class OrderTableAdmin(admin.ModelAdmin):
    list_display = ("orderId", "product", "subtotal")


@admin.register(FinalOrderTable)
class finalOrderTableAdmin(admin.ModelAdmin):
    list_display = (
        "orderId", "no_of_products", "total_price", "razorpay_orderId", "razorpay_paymentId",
        "razorpay_signatureId")
