from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from sportscenter.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.contrib import messages
from TurfBookingApp.models import TurfBookingTable
import razorpay
from django.views import View
from django.views.decorators.csrf import csrf_exempt


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


def paypal_cancel(request):
    messages.error(request, "Your booking has been cancelled")
    print(".failed")
    return redirect('turf_homepage')
