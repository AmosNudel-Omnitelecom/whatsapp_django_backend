from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_wabas, name='get_wabas'),
    path('client/', views.get_client_wabas, name='get_client_wabas'),
    path('phone-numbers/', views.get_waba_phone_numbers, name='get_waba_phone_numbers'),
    path('phone-numbers/register/', views.register_phone_number, name='register_phone_number'),
    path('webhook-subscribe/', views.subscribe_webhook, name='subscribe_webhook'),
    path('webhook-subscriptions/', views.get_waba_webhook_subscriptions, name='get_waba_webhook_subscriptions'),
]
