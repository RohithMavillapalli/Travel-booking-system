from django.urls import path
from . import views

urlpatterns = [

    path('add-flight/', views.add_flight, name="add_flight"),
    path('search-flights/', views.search_flights, name="search_flights"),
    path('edit-flight/<int:flight_id>/', views.edit_flight, name="edit_flight"),
    path('delete-flight/<int:flight_id>/', views.delete_flight, name="delete_flight"),


]