from django.urls import path
from . import views

urlpatterns = [
    path('get-numbers/', views.get_phone_numbers, name='get_phone_numbers'),
    path('add/', views.add_phone_number, name='add_phone_number'),
    # path('delete/<str:phone_number_id>/', views.delete_phone_number, name='delete_phone_number'),
    path('request-code/', views.request_verification_code, name='request_verification_code'),
    path('verify-code/', views.verify_code, name='verify_code'),
    path('single/', views.get_single_phone_number, name='get_single_phone_number'),
]