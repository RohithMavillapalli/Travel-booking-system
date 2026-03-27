from django.urls import path
from . import views

urlpatterns = [

    path('book-flight/<int:flight_id>/', views.book_flight, name="book_flight"),
    path('my-bookings/', views.my_bookings, name="my_bookings"),
    path('flight-bookings/<int:flight_id>/', views.flight_bookings, name="flight_bookings"),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name="cancel_booking"),
    path('ticket/<int:booking_id>/', views.view_ticket, name="ticket"),
    
]