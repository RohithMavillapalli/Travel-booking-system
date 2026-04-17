from django.shortcuts import render,redirect
from accounts.models import User
from flights.models import Flight
from bookings.models import Booking
# Create your views here.
def admin_users(request):
    users = User.objects.all()
    return render(request, "admin_users.html", {"users": users})


def register(request):

    if request.method == "POST":

        role = request.POST['role']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        user = User(
            role=role,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password
        )

        user.save()

        return redirect('/login/')

    return render(request,"register.html")

def login(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)

            request.session['user_id'] = user.user_id
            request.session['role'] = user.role
            request.session['first_name'] = user.first_name
            if user.role == "traveller":
                return redirect('/traveller-dashboard/')
            elif user.role == "provider":
                return redirect('/provider-dashboard/')
            elif user.role == "admin":
                return redirect('/admin-dashboard/')
        except:
            return render(request,"login.html",{'error':"Invalid Login"})

    return render(request,"login.html")

def logout(request):

    request.session.flush()

    return redirect('/')


def update_profile(request):

    user_id = request.session.get('user_id')

    user = User.objects.get(user_id=user_id)

    if request.method == "POST":

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.password = request.POST['password']

        user.save()

        return redirect('/traveller-dashboard/')

    return render(request, "update_profile.html", {"user": user})

#admin dashboard
def admin_dashboard(request):
    total_users = User.objects.count()
    total_flights = Flight.objects.count()
    total_bookings = Booking.objects.count()

    users = User.objects.all()[:5]
    flights = Flight.objects.all()[:5]
    bookings = Booking.objects.all()[:5]

    context = {
        'total_users': total_users,
        'total_flights': total_flights,
        'total_bookings': total_bookings,
        'users': users,
        'flights': flights,
        'bookings': bookings,
    }

    return render(request, 'admin_dashboard.html', context)

def admin_logout(request):
    # remove custom session values
    if 'user_id' in request.session:
        del request.session['user_id']

    if 'role' in request.session:
        del request.session['role']

    # optional: clear everything
    request.session.flush()

    return redirect('home')