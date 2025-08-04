from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_wabas(request):
    try:
        if not getattr(settings, 'ACCESS_TOKEN', None):
            return Response(
                {"error": "ACCESS_TOKEN not found in environment variables"}, 
                status=400
            )
        if not getattr(settings, 'BUSINESS_PORTFOLIO_ID', None):
            return Response(
                {"error": "BUSINESS_PORTFOLIO_ID not found in environment variables"}, 
                status=400
            )
        
        access_token = getattr(settings, 'ACCESS_TOKEN', None)
        business_portfolio_id = getattr(settings, 'BUSINESS_PORTFOLIO_ID', None)

        url = f"https://graph.facebook.com/v23.0/{business_portfolio_id}/owned_whatsapp_business_accounts"

        params = {
            "access_token": access_token
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return Response({
                "error": f"Facebook API error: {response.status_code}",
                "details": response.text,
                "url": url
            }, status=response.status_code)
        
        return Response(response.json())
    
    except Exception as e:
        return Response(
            {"error": f"Failed to get wabas: {str(e)}"}, 
            status=500
        )

@api_view(['GET'])
def get_client_wabas(request):
    try:
        if not getattr(settings, 'ACCESS_TOKEN', None):
            return Response(
                {"error": "ACCESS_TOKEN not found in environment variables"}, 
                status=400
            )
        if not getattr(settings, 'BUSINESS_PORTFOLIO_ID', None):
            return Response(
                {"error": "BUSINESS_PORTFOLIO_ID not found in environment variables"}, 
                status=400
            )
        
        access_token = getattr(settings, 'ACCESS_TOKEN', None)
        business_portfolio_id = getattr(settings, 'BUSINESS_PORTFOLIO_ID', None)

        url = f"https://graph.facebook.com/v23.0/{business_portfolio_id}/client_whatsapp_business_accounts"

        params = {
            "access_token": access_token,
            "filtering": f'[{{"field":"partners","operator":"ALL","value":["{business_portfolio_id}"]}}]'
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return Response({
                "error": f"Facebook API error: {response.status_code}",
                "details": response.text,
                "url": url
            }, status=response.status_code)
        
        return Response(response.json())
    
    except Exception as e:
        return Response(
            {"error": f"Failed to get client wabas: {str(e)}"}, 
            status=500
        )
    
@api_view(['GET'])
def get_waba_phone_numbers(request):
    try:
        if not getattr(settings, 'ACCESS_TOKEN', None):
            return Response(
                {"error": "ACCESS_TOKEN not found in environment variables"}, 
                status=400
            )
        access_token = getattr(settings, 'ACCESS_TOKEN', None)
        waba_id = request.query_params.get('waba_id')

        url = f"https://graph.facebook.com/v23.0/{waba_id}/phone_numbers"

        params = {
            "access_token": access_token
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return Response({
                "error": f"Facebook API error: {response.status_code}",
                "details": response.text,
                "url": url
            }, status=response.status_code)
        
        return Response(response.json())
    
    except Exception as e:
        return Response(
            {"error": f"Failed to get waba phone numbers: {str(e)}"}, 
            status=500
        )