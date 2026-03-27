from django.shortcuts import render
from flights.models import Flight
# Create your views here.
def traveller_dashboard(request):

    flights = Flight.objects.all()

    return render(request, "traveller_dashboard.html", {'flights': flights})


def provider_dashboard(request):

    provider_id = request.session.get('user_id')

    flights = Flight.objects.filter(provider_id=provider_id)

    return render(request, "provider_dashboard.html", {'flights': flights})