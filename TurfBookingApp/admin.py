from django.contrib import admin
from .models import *
from django import forms


# Register your models here.


@admin.register(TurfDetails)
class TurfDetailsAdmin(admin.ModelAdmin):
    list_display = ("turf_name", "category", "turf_morningPrice", "turf_eveningPrice")


@admin.register(FootballTimeSlotTable)
class FootballTimeSlotTable(admin.ModelAdmin):
    list_display = ("time_slot", "price")
    ordering = ['id']


@admin.register(ShuttleTimeSlotTable)
class ShuttleTimeSlotTable(admin.ModelAdmin):
    list_display = ("time_slot", "price")
    ordering = ['id']


@admin.register(CricketTimeSlotTable)
class CricketTimeSlotTable(admin.ModelAdmin):
    list_display = ("time_slot", "price")
    ordering = ['id']


@admin.register(TurfReviewTable)
class TurfReviewTable(admin.ModelAdmin):
    ordering = ['id']


@admin.register(TurfBookingTable)
class TurfBookingTableAdmin(admin.ModelAdmin):
    list_display = ("turf_name", "booking_date", "time_slot", "amount", "payment_id")

# @admin.register(FootballTimeSlotTable)
# class FootballTimeSlotTableAdmin(admin.ModelAdmin):
#     def __init__(self, *args, **kwargs):
#         try:
#             turf_name = kwargs['instance'].turf_name
#         except KeyError:
#             turf_name = 1
#         #super(FootballTimeSlotTableAdmin, self).__init__(*args, **kwargs)
#         self.fields['price'].queryset = TurfDetails.objects.filter(turf_name=turf_name)
