from django.shortcuts import render,redirect,get_object_or_404
from .models import Booking
from flights.models import Flight
# Create your views here.


def book_flight(request, flight_id):

    flight = Flight.objects.get(flight_id=flight_id)

    if request.method == "POST":

        passenger_count = int(request.POST['passenger_count'])

        # limit booking to 6 passengers
        if passenger_count > 6:
            return render(request, "book_flight.html", {
                "flight": flight,
                "error": "Maximum 6 passengers allowed per booking"
            })

        # check seat availability
        if flight.seats < passenger_count:
            return render(request, "book_flight.html", {
                "flight": flight,
                "error": "Not enough seats available"
            })

        user_id = request.session.get('user_id')

        # create booking for each passenger
        for i in range(1, passenger_count + 1):

            name = request.POST.get(f'name_{i}')
            age = request.POST.get(f'age_{i}')
            gender = request.POST.get(f'gender_{i}')

            Booking.objects.create(
                user_id=user_id,
                flight_id=flight_id,
                passenger_name=name,
                passenger_age=age,
                passenger_gender=gender
            )

        # reduce seats after booking
        flight.seats -= passenger_count
        flight.save()

        return redirect('/my-bookings/')

    return render(request, "book_flight.html", {"flight": flight})

def my_bookings(request):

    user_id = request.session.get('user_id')

    bookings = Booking.objects.filter(user_id=user_id)

    booking_details = []

    for booking in bookings:

        flight = Flight.objects.get(flight_id=booking.flight_id)

        booking_details.append({
            'booking': booking,
            'flight': flight
        })

    return render(request, "my_bookings.html", {'booking_details': booking_details})

def flight_bookings(request, flight_id):

    bookings = Booking.objects.filter(flight_id=flight_id)

    return render(request,"flight_bookings.html",{'bookings':bookings})


def cancel_booking(request, booking_id):

    booking = get_object_or_404(Booking, booking_id=booking_id)

    flight = Flight.objects.get(flight_id=booking.flight_id)

    # increase seat back
    flight.seats += 1
    flight.save()

    booking.delete()

    return redirect('/my-bookings/')


def view_ticket(request, booking_id):

    booking = Booking.objects.get(booking_id=booking_id)

    flight = Flight.objects.get(flight_id=booking.flight_id)

    return render(request,"ticket.html",{
        'booking': booking,
        'flight': flight
    })