from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from sportscenter.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.contrib import messages
from TurfBookingApp.models import TurfBookingTable
import razorpay

# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


def turf_payment(request):
    turf_order_id = request.session.get('turfOrder_id')
    turf_order = get_object_or_404(TurfBookingTable, id=turf_order_id)

    price = int(turf_order.amount) * 100
    DATA = {
        "amount": price,
        "currency": "INR",
        "receipt": str(turf_order_id),
        "notes": {
            "order_type": "basic order",
            "key2": "value2",
        },
        'payment_capture': 0

    }
    # payment_order = client.order.create(data=DATA)
    # print("----------------------",payment_order)
    # payment_order_id = payment_order['id']
    context = {'amount': price, 'order_id': turf_order_id, 'api_key': RAZORPAY_API_KEY}
    return render(request, 'turf_PaymentPage.html', context)


def paypal_done(request):
    messages.success(request, "You've successfully made a payment")
    return redirect('turf_homepage')


def paypal_cancel(request):
    messages.error(request, "Your booking has been cancelled")
    return redirect('turf_homepage')
