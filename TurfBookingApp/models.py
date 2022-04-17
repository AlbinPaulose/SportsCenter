from django.contrib.auth.models import User
from django.db import models

# Create your models here.
book_status = (
    ("Pending", "pending"),
    ("Success", "success"),
    ("Failed", "failed"),
    ("Cancelled", "cancelled"),
    ("Refunded", "refunded")
)

turf_category = (
    ("football", "Football"),
    ("shuttle", "Shuttle"),
    ("cricket", "Cricket")
)


# Create your models here.
class TurfDetails(models.Model):
    category = models.CharField(max_length=20, choices=turf_category)
    turf_name = models.CharField(max_length=50)
    turf_place = models.CharField(max_length=50)
    turf_morningPrice = models.IntegerField()
    turf_eveningPrice = models.IntegerField()
    turf_phoneNumber = models.CharField(max_length=10)
    turf_address = models.CharField(max_length=70)

    def __str__(self):
        return str(self.turf_name)


class FootballTimeSlotTable(models.Model):
    turf_name = models.ForeignKey(TurfDetails, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.IntegerField(default=1)
    available = models.BooleanField(default=True)


class TurfBookingTable(models.Model):
    category = models.CharField(max_length=15)
    turf_name = models.ForeignKey(TurfDetails, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    hours_need = models.IntegerField(default=1)
    booking_date = models.DateField()
    time_slot = models.CharField(max_length=30)
    amount = models.IntegerField()
    note = models.TextField(blank=True)
    payment_id = models.CharField(blank=True,max_length=100)
    book_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class ShuttleTimeSlotTable(models.Model):
    turf_name = models.ForeignKey(TurfDetails, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.IntegerField(default=1)
    available = models.BooleanField(default=True)


class CricketTimeSlotTable(models.Model):
    turf_name = models.ForeignKey(TurfDetails, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.IntegerField(default=1)
    available = models.BooleanField(default=True)


class TurfReviewTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf_name = models.ForeignKey(TurfDetails, on_delete=models.CASCADE)
    rating = models.CharField(max_length=15)
    feedback = models.TextField(blank=True)
    image = models.ImageField(upload_to='review_images')
    reviewed_at = models.DateField(auto_now_add=True)
