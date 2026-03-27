from django.db import models
from accounts.models import User
from flights.models import Flight
# Create your models here.
class Booking(models.Model):

    booking_id = models.AutoField(primary_key=True)

    user_id = models.IntegerField()

    flight_id = models.IntegerField()

    passenger_name = models.CharField(max_length=100)

    passenger_age = models.IntegerField()

    passenger_gender = models.CharField(max_length=10)

    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bookings"

        