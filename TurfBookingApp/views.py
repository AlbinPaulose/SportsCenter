from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from django.db.models import Subquery

# Create your views here.
"""TURF HOME PAGE"""


def turf_home_page(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            user_details = User.objects.get(id=userid)
            reviews = TurfReviewTable.objects.all().order_by('-id')[:5]
            return render(request, "turf_HomePage.html", {'user': user_details, 'reviews': reviews})


""" VIEW FOOTBALL TURF BOOKING PAGE """


def football_booking_page(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            user_details = User.objects.get(id=userid)
            turf_details = TurfDetails.objects.filter(category='football')
            return render(request, 'turf_FootballBookingPage.html', {'userDetails': user_details, 'turf': turf_details})
        else:
            return redirect('login_redirect_turf')


"AJAX FUNCTION TO GET AVAILABLE TIME SLOT OF FOOTBALL TURF "


def available_time_slot_football(request):
    date_value = request.GET.get('date_value')
    turf = TurfDetails.objects.get(category='football')
    booked_timeSlot = TurfBookingTable.objects.filter(category='football', turf_name=turf,
                                                      booking_date=date_value, book_status='pending')
    time_slots = FootballTimeSlotTable.objects.exclude(
        time_slot__in=Subquery(booked_timeSlot.values('time_slot'))) & FootballTimeSlotTable.objects.filter(
        available=True).order_by('id')
    return JsonResponse(list(time_slots.values('time_slot')), safe=False)


"AJAX FUNCTION TO GET CORRESPONDING PRICE ACCORDING TO TIME SLOT SELECTED IN FOOTBALL TURF "


def get_price_football(request):
    time_id = request.GET.get('time_id')
    time_object = FootballTimeSlotTable.objects.filter(time_slot=time_id)
    for data in time_object:
        price = data.price
    return JsonResponse(price, safe=False)


"""BOOK THE TIME SLOT OF FOOTBALL"""


def book_football_turf(request):
    book = False
    if request.method == 'POST':
        userid = request.session['userid']
        user_id = User.objects.get(id=userid)
        phone = request.POST["visitor_phone"]
        no_of_hours = request.POST["total_hours"]
        booking_date = request.POST["book_date"]
        timeslot = request.POST["hour_preference"]
        note = request.POST["message"]
        amount = request.POST["total_amount"]
        turf = TurfDetails.objects.get(category='football')
        if TurfBookingTable.objects.filter(booking_date=booking_date, time_slot=timeslot, category='football',
                                           turf_name=turf).exists():
            messages.info(request, 'Already Booked')
            return redirect('turf_FootballBooking')
        else:
            booking = TurfBookingTable.objects.create(userid=user_id, phone=phone, hours_need=no_of_hours,
                                                      booking_date=booking_date, time_slot=timeslot,
                                                      amount=amount, note=note, category='football',
                                                      turf_name=turf, book_status='pending')
            booking.save()
            request.session['turfOrder_id'] = booking.id
            return redirect('../payment/turf_payment')
    return render(request, 'turf_FootballBookingPage.html', {'booked': book})


"""VIEW SHUTTLE TURF BOOKING PAGE"""


def shuttle_booking_page(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            user_details = User.objects.get(id=userid)
            turf_details = TurfDetails.objects.filter(category='shuttle')
            return render(request, 'turf_ShuttleBookingPage.html', {'userDetails': user_details, 'turf': turf_details})
        else:
            return redirect('login_redirect_turf')


"AJAX FUNCTION TO GET AVAILABLE TIME SLOT OF SHUTTLE TURF "


def available_time_slot_shuttle(request):
    date_value = request.GET.get('date_value')
    turf = TurfDetails.objects.get(category='shuttle')
    booked_timeSlot = TurfBookingTable.objects.filter(category='shuttle', turf_name=turf,
                                                      booking_date=date_value, book_status='pending')
    time_slots = ShuttleTimeSlotTable.objects.exclude(
        time_slot__in=Subquery(booked_timeSlot.values('time_slot'))) & ShuttleTimeSlotTable.objects.filter(
        available=True).order_by('id')
    return JsonResponse(list(time_slots.values('time_slot')), safe=False)


"AJAX FUNCTION TO GET CORRESPONDING PRICE ACCORDING TO TIME SLOT SELECTED IN SHUTTLE TURF "


def get_price_shuttle(request):
    time_id = request.GET.get('time_id')
    time_object = ShuttleTimeSlotTable.objects.filter(time_slot=time_id)
    for data in time_object:
        price = data.price
    return JsonResponse(price, safe=False)


"""BOOK THE TIME SLOT OF SHUTTLE"""


def book_shuttle_turf(request):
    if request.method == 'POST':
        userid = request.session['userid']
        user_id = User.objects.get(id=userid)
        phone = request.POST["visitor_phone"]
        no_of_hours = request.POST["total_hours"]
        booking_date = request.POST["book_date"]
        timeslot = request.POST["hour_preference"]
        note = request.POST["message"]
        amount = request.POST["total_amount"]
        turf = TurfDetails.objects.get(category='shuttle')
        if TurfBookingTable.objects.filter(booking_date=booking_date, time_slot=timeslot, category='shuttle',
                                           turf_name=turf).exists():
            messages.info(request, 'Already Booked')
            return redirect('turf_ShuttleBooking')
        else:
            booking = TurfBookingTable.objects.create(userid=user_id, phone=phone, hours_need=no_of_hours,
                                                      booking_date=booking_date, time_slot=timeslot,
                                                      amount=amount, note=note, category='shuttle',
                                                      turf_name=turf, book_status='pending')
            booking.save()
            request.session['turfOrder_id'] = booking.id
            return redirect('../payment/turf_payment')
    return render(request, 'turf_ShuttleBookingPage.html')


"""VIEW CRICKET  TURF BOOKING PAGE"""


def cricket_booking_page(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            user_details = User.objects.get(id=userid)
            turf_details = TurfDetails.objects.filter(category='cricket')
            return render(request, 'turf_CricketBookingPage.html', {'userDetails': user_details, 'turf': turf_details})
        else:
            return redirect('login_redirect_turf')


"AJAX FUNCTION TO GET AVAILABLE TIME SLOT OF CRICKET TURF "


def available_time_slot_cricket(request):
    date_value = request.GET.get('date_value')
    turf = TurfDetails.objects.get(category='cricket')
    booked_timeSlot = TurfBookingTable.objects.filter(category='cricket', turf_name=turf,
                                                      booking_date=date_value, book_status='pending')
    time_slots = CricketTimeSlotTable.objects.exclude(
        time_slot__in=Subquery(booked_timeSlot.values('time_slot'))) & CricketTimeSlotTable.objects.filter(
        available=True).order_by('id')
    return JsonResponse(list(time_slots.values('time_slot')), safe=False)


"AJAX FUNCTION TO GET CORRESPONDING PRICE ACCORDING TO TIME SLOT SELECTED IN CRICKET TURF "


def get_price_cricket(request):
    time_id = request.GET.get('time_id')
    time_object = CricketTimeSlotTable.objects.filter(time_slot=time_id)
    for data in time_object:
        price = data.price
    return JsonResponse(price, safe=False)


"""BOOK THE TIME SLOT OF CRICKET"""


def book_cricket_turf(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        if request.method == 'POST':
            userid = request.session['userid']
            user_id = User.objects.get(id=userid)
            phone = request.POST["visitor_phone"]
            no_of_hours = request.POST["total_hours"]
            booking_date = request.POST["book_date"]
            timeslot = request.POST["hour_preference"]
            note = request.POST["message"]
            amount = request.POST["total_amount"]
            turf = TurfDetails.objects.get(category='cricket')
            if TurfBookingTable.objects.filter(booking_date=booking_date, time_slot=timeslot, category='cricket',
                                               turf_name=turf).exists():
                messages.info(request, 'Already Booked')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                booking = TurfBookingTable.objects.create(userid=user_id, phone=phone, hours_need=no_of_hours,
                                                          booking_date=booking_date, time_slot=timeslot,
                                                          amount=amount, note=note, category='cricket',
                                                          turf_name=turf, book_status='pending')
                booking.save()
                request.session['turfOrder_id'] = booking.id
                return redirect('../payment/turf_payment')
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'turf_CricketBookingPage.html')


""" ORDER HISTORY PAGE """


def order_history(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        userid = request.session['userid']
        first_name = User.objects.get(id=userid)
        items = TurfBookingTable.objects.filter(userid=userid).order_by('-id')
        if items is not None:
            for orders in items:
                if orders.id is not None:
                    return render(request, 'turf_OrderHistory.html', {'orders': items, 'user': first_name})
            messages.info(request, 'Not Yet Booked Anything!!!')
            return render(request, 'turf_OrderHistory.html', {'user': first_name})


""" CODE TO CANCEL ORDER"""


def cancel_order(request, oid):
    TurfBookingTable.objects.filter(id=oid).update(book_status='cancelled')
    cancelled = True
    return redirect(order_history)


"""REVIEW PAGE CODE"""


def review(request):
    if 'userid' not in request.session:
        return redirect('login_redirect_turf')
    else:
        userid = request.session['userid']
        user = User.objects.get(id=userid)
        turf = TurfDetails.objects.all()
        reviews = TurfReviewTable.objects.all().order_by('-id')
        if request.method == 'POST':
            turf_name = request.POST["turf_name"]
            rating = request.POST["rating"]
            feedback = request.POST["feedback"]
            image = request.POST["review_image"]
            turf = TurfDetails.objects.get(turf_name=turf_name)
            new_review = TurfReviewTable.objects.create(user=user, turf_name=turf, rating=rating, feedback=feedback,
                                                        image=image)
            new_review.save()
            return redirect('turf_review')
        return render(request, 'turf_ReviewPage.html', {'user': user, 'turf_name': turf, 'reviews': reviews})


"""LOGIN REDIRECT TO SAME PAGE"""


def login_redirect_turf(request):
    print("..............login to continue.....")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['userid'] = user.id
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return redirect('turf/turf_homepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login_redirect_turf')
    else:
        return render(request, 'turf_LoginPage.html')
