from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from TurfBookingApp.models import TurfReviewTable
from .models import *

""" TURF BOOKING INDEX PAGE(FIRST PAGE)"""


def turf_index(request):
    reviews = TurfReviewTable.objects.all().order_by('-id')[:5]
    return render(request, "turf_index.html", {'reviews': reviews})


"""LOG IN CODE FOR TURF BOOKING ALONG"""


def login_turf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['userid'] = user.id
            return redirect('../turf/turf_homepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login_turf')
    else:
        return render(request, 'turf_LoginPage.html')
