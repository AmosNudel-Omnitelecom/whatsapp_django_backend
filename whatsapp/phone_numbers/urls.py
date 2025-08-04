from django.urls import path
from . import views

urlpatterns = [
    path('phone-numbers/', views.get_phone_numbers, name='get_phone_numbers'),
    path('phone-numbers/add/', views.add_phone_number, name='add_phone_number'),
    path('phone-numbers/delete/', views.delete_phone_number, name='delete_phone_number'),
    path('phone-numbers/request-code/', views.request_verification_code, name='request_verification_code'),
]