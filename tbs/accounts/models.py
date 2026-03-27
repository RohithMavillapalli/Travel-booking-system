from django.db import models

# Create your models here.
class User(models.Model):

    ROLE_CHOICES = (
        ('traveller','Traveller'),
        ('provider','Provider'),
        ('admin','Admin'),
    )

    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    password = models.CharField(max_length=255)

    class Meta:
        db_table = "users"