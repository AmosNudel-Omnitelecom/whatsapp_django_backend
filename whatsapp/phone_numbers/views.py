from django.shortcuts import render
from django.conf import settings
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_phone_numbers(request):
    try:
        # Use business portfolio ID from settings
        business_portfolio_id = getattr(settings, 'BUSINESS_PORTFOLIO_ID', None)
        if not business_portfolio_id:
            return Response(
                {"error": "BUSINESS_PORTFOLIO_ID not found in environment variables"}, 
                status=400
            )
            
        # Facebook Graph API endpoint - use preverified_numbers endpoint
        url = f"https://graph.facebook.com/v23.0/{business_portfolio_id}/preverified_numbers"
        
        # Get access token from settings
        access_token = getattr(settings, 'ACCESS_TOKEN', None)
        if not access_token:
            return Response(
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
            return Response({
                "error": f"Facebook API error: {response.status_code}",
                "details": response.text,
                "url": url
            }, status=response.status_code)
            
        return Response(response.json())
        
    except Exception as e:
        return Response(
            {"error": f"Failed to retrieve phone numbers: {str(e)}"}, 
            status=500
        )
    
@api_view(['POST'])
def add_phone_number(request):
    try:
        phone_number = request.data.get('phone_number')
        business_portfolio_id = getattr(settings, 'BUSINESS_PORTFOLIO_ID', None)
        access_token = getattr(settings, 'ACCESS_TOKEN', None)
        if not business_portfolio_id:
            print("BUSINESS_PORTFOLIO_ID not found in environment variables")
            return Response(
                {"error": "BUSINESS_PORTFOLIO_ID not found in environment variables"}, 
                status=400
            )
        
        url = f"https://graph.facebook.com/v23.0/{business_portfolio_id}/add_phone_numbers"
        
        data = {
            "phone_number": phone_number
        }

        params = {
            "access_token": access_token
        }

        response = requests.post(url, json=data, params=params)

        if response.status_code != 200:
            return Response({
                "error": f"Facebook API error: {response.status_code}",
                "details": response.text,
                "url": url
            }, status=response.status_code)
            
        return Response(response.json())
    
    except Exception as e:
        return Response(
            {"error": f"Failed to add phone number: {str(e)}"}, 
            status=500
        )
    
    


