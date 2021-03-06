import json
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from sportscenter.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.contrib import messages
from TurfBookingApp.models import TurfBookingTable
from SportsStoreApp.models import FinalOrderTable, CartTable, OrderTable
from Index.models import ProductsDetails
import razorpay
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.


class Turf_payment(View):
    def get(self, request):
        turf_order_id = request.session.get('turfOrder_id')
        turf_order = get_object_or_404(TurfBookingTable, id=turf_order_id)
        price = int(turf_order.amount) * 100
        client = razorpay.Client(
            auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

        payment = client.order.create({'amount': price, 'currency': 'INR',
                                       'payment_capture': '1'})
        payment_order_id = payment['id']
        print(".............", payment_order_id)
        print("...............", turf_order_id)
        context = {'amount': price, 'payment_id': payment_order_id, 'api_key': RAZORPAY_API_KEY,
                   'order_id': turf_order_id}
        return render(request, 'turf_PaymentPage.html', context)


@csrf_exempt
def turf_payment_success(request, order_id, payment_id):
    TurfBookingTable.objects.filter(id=order_id).update(payment_id=payment_id, book_status='success')
    return render(request, 'turf_PaymentSuccessPage.html')


def sports_store_payment(request):
    store_order_id = request.session.get('storeOrder_id')
    store_order = get_object_or_404(FinalOrderTable, orderId=store_order_id)
    price = int(store_order.total_price) * 100
    client = razorpay.Client(
        auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

    payment = client.order.create({'amount': price, 'currency': 'INR',
                                   'payment_capture': '1'})
    payment_order_id = payment['id']
    print(".............", payment_order_id)
    FinalOrderTable.objects.filter(orderId=store_order_id).update(razorpay_orderId=payment_order_id)
    context = {'amount': price, 'payment_id': payment_order_id, 'api_key': RAZORPAY_API_KEY,
               'order_id': store_order_id, 'callback_url': "http://" + "127.0.0.1:8000" + "/payment/callback/", }
    return render(request, "store_PaymentPage.html", context)


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = FinalOrderTable.objects.get(razorpay_orderId=provider_order_id)
        order.razorpay_paymentId = payment_id
        order.razorpay_signatureId = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = 'success'
            order.save()
            return render(request, "store_Callback.html", {"status": order.status})
        else:
            order_id = order.orderId
            OrderTable.objects.filter(orderId=order_id).update(status='processing')
            orders = OrderTable.objects.filter(orderId=order_id)
            for order in orders:
                product_id = order.product
                qty = order.quantity
                product = ProductsDetails.objects.get(id=product_id.id)
                product.product_stock = int(product.product_stock)-int(qty)
                product.save()
            user = order.user
            CartTable.objects.filter(user_id=user.id).delete()
            FinalOrderTable.objects.filter(orderId=order_id).update(status='success')
            OrderTable.objects.filter(orderId=order_id).update(status='success')
            return render(request, "store_Callback.html", {"status": 'success'})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = FinalOrderTable.objects.get(razorpay_orderId=provider_order_id)
        order.razorpay_paymentId = payment_id
        order.razorpay_orderId = provider_order_id
        order.status = 'failed'
        order.save()
        order_id = order.orderId
        OrderTable.objects.filter(orderId=order_id).update(status='failed')
        return render(request, "store_Callback.html", {"status": order.status})


