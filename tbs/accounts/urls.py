from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('update-profile/', views.update_profile, name="update_profile"),
    path('admin-users/', views.admin_users, name="admin_users"),
    path('logout/', views.admin_logout, name='admin_logout'),
]