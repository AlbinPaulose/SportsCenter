from django.urls import path, include
from . import views

urlpatterns = [
    path('turf_payment', views.Turf_payment.as_view(), name="turf_payment"),
    path('turf_paymentSuccess/<int:order_id>/<str:payment_id>/', views.turf_payment_success,
         name="turf_paymentSuccess"),
    path('store_payment', views.sports_store_payment, name="store_payment"),
    path("callback/", views.callback, name="callback"),

]
