from django.urls import path, include
from . import views

urlpatterns = [
    path('turf_payment', views.turf_payment, name="turf_payment"),
    path('paypal-done', views.paypal_done, name="paypal-done"),
    path('paypal-cancel', views.paypal_cancel, name="paypal-cancel"),

]