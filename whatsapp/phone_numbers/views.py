from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import requests
import json

# Create your views here.

def get_phone_numbers(request):
    """
    Django view to retrieve phone numbers from Facebook Graph API
    """
    try:
        # Use business portfolio ID from settings
        business_portfolio_id = getattr(settings, 'BUSINESS_PORTFOLIO_ID', None)
        if not business_portfolio_id:
            return JsonResponse(
                {"error": "BUSINESS_PORTFOLIO_ID not found in environment variables"}, 
                status=400
            )
            
        # Facebook Graph API endpoint - use preverified_numbers endpoint
        url = f"https://graph.facebook.com/v23.0/{business_portfolio_id}/preverified_numbers"
        
        # Get access token from settings
        access_token = getattr(settings, 'ACCESS_TOKEN', None)
        if not access_token:
            return JsonResponse(
                {"error": "ACCESS_TOKEN not found in environment variables"}, 
                status=400
            )
        
        # Add access token and fields to request parameters
        params = {
            "access_token": access_token,
            "fields": "id,phone_number,code_verification_status,verification_expiry_time"
        }
        
        # Make the request to Facebook Graph API
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return JsonResponse({
                "error": f"Facebook API error: {response.status_code}",
                "details": response.text,
                "url": url
            }, status=response.status_code)
            
        return JsonResponse(response.json())
        
    except Exception as e:
        return JsonResponse(
            {"error": f"Failed to retrieve phone numbers: {str(e)}"}, 
            status=500
        )



