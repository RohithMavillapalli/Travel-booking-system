from django.shortcuts import render,redirect, get_object_or_404
from .models import Flight
# Create your views here.

def add_flight(request):

    if request.method == "POST":

        flight_number = request.POST['flight_number']
        airline_name = request.POST['airline_name']
        source = request.POST['source']
        destination = request.POST['destination']
        departure_time = request.POST['departure_time']
        arrival_time = request.POST['arrival_time']
        price = request.POST['price']
        seats = request.POST['seats']

        provider_id = request.session.get('user_id')

        flight = Flight(
            provider_id=provider_id,
            flight_number=flight_number,
            airline_name=airline_name,
            source=source,
            destination=destination,
            departure_time=departure_time,
            arrival_time=arrival_time,
            price=price,
            seats=seats
        )

        flight.save()

        return redirect('/provider-dashboard/')

    return render(request,"add_flight.html")

def search_flights(request):

    source = request.GET.get('source')
    destination = request.GET.get('destination')

    flights = Flight.objects.all()

    if source and destination:

        flights = Flight.objects.filter(source=source, destination=destination)

    return render(request,"search_flights.html",{'flights':flights})


def edit_flight(request, flight_id):

    flight = get_object_or_404(Flight, flight_id=flight_id)

    if request.method == "POST":

        flight.flight_number = request.POST['flight_number']
        flight.airline_name = request.POST['airline_name']
        flight.source = request.POST['source']
        flight.destination = request.POST['destination']
        flight.departure_time = request.POST['departure_time']
        flight.arrival_time = request.POST['arrival_time']
        flight.price = request.POST['price']
        flight.seats = request.POST['seats']

        flight.save()

        return redirect('/provider-dashboard/')

    return render(request,"edit_flight.html",{'flight':flight})

def delete_flight(request, flight_id):

    flight = get_object_or_404(Flight, flight_id=flight_id)

    flight.delete()

    return redirect('/provider-dashboard/')