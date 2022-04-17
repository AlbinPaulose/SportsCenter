from django.urls import path, include
from . import views

urlpatterns = [
    path('turf_payment', views.Turf_payment.as_view(), name="turf_payment"),
    path('turf_paymentSuccess/<int:order_id>/<str:payment_id>/', views.turf_payment_success,
         name="turf_paymentSuccess"),
    path('paypal-cancel', views.paypal_cancel, name="paypal-cancel"),

]
