from django.urls import path
from . import views

urlpatterns = [
    path('phone-numbers/', views.get_phone_numbers, name='get_phone_numbers'),
    path('phone-numbers/add/', views.add_phone_number, name='add_phone_number'),
]