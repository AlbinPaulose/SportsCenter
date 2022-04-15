from django.urls import path, include
from . import views

urlpatterns = [
    path('turf_homepage', views.turf_home_page, name="turf_homepage"),
    path('login_redirect_turf', views.login_redirect_turf, name="login_redirect_turf"),
    path('turf_FootballBooking', views.football_booking_page, name="turf_FootballBooking"),
    path('ajax/load_available_timeSlot/', views.available_time_slot_football, name='ajax_load_available_timeSlot'),
    path('ajax/load-price/', views.get_price_football, name='ajax_load_price'),  # AJAX
    path('book_football_turf', views.book_football_turf, name="book_football_turf"),
    path('turf_ShuttleBooking', views.shuttle_booking_page, name="turf_ShuttleBooking"),
    path('ajax/load_available_shuttleTimeSlot/', views.available_time_slot_shuttle,
         name='ajax_load_available_shuttleTimeSlot'),
    path('ajax/shuttle_price/', views.get_price_shuttle, name='load_price_shuttle'),
    path('book_shuttle_turf', views.book_shuttle_turf, name="book_shuttle_turf"),
    path('turf_CricketBooking', views.cricket_booking_page, name="cricket_ShuttleBooking"),
    path('ajax-load_available_cricketTimeSlot', views.available_time_slot_cricket,
         name='ajax-load_available_cricketTimeSlot'),
    path('ajax-cricket_price', views.get_price_cricket, name='ajax-cricket_price'),
    path('book_cricket_turf', views.book_cricket_turf, name="book_cricket_turf"),
    path('order_history', views.order_history, name="order_history"),
    path('cancel_order/<int:oid>/', views.cancel_order, name="cancel_order"),
    path('turf_review', views.review, name="turf_review"),
]
