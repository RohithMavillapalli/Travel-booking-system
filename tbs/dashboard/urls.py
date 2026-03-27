from django.urls import path
from . import views

urlpatterns = [

    path('traveller-dashboard/', views.traveller_dashboard, name="traveller_dashboard"),

    path('provider-dashboard/', views.provider_dashboard, name="provider_dashboard"),

]