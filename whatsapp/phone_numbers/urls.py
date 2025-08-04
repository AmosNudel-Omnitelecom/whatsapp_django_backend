from django.urls import path
from . import views

urlpatterns = [
    path('phone-numbers/', views.get_phone_numbers, name='get_phone_numbers'),
]