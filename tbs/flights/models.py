from django.db import models
from accounts.models import User
# Create your models here.
class Flight(models.Model):

    flight_id = models.AutoField(primary_key=True)

    provider_id = models.IntegerField()

    flight_number = models.CharField(max_length=20)

    airline_name = models.CharField(max_length=100)

    source = models.CharField(max_length=100)

    destination = models.CharField(max_length=100)

    departure_time = models.DateTimeField()

    arrival_time = models.DateTimeField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    seats = models.IntegerField()

    class Meta:
        db_table = "flights"

