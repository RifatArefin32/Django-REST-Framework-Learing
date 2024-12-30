# views.py
from faker import Faker
from decimal import Decimal
import requests # type: ignore
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_first_app.serializers import CurrencyConversionSerializer, CategorySerializer
from drf_first_app.models import Category


"""
Class based view
"""
class CurrencyConversionAPIView(APIView):
    def post(self, request):
        serializer = CurrencyConversionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            from_currency = serializer.validated_data['from_currency'].upper()
            to_currency = serializer.validated_data['to_currency'].upper()

            # Fetch exchange rate from an external API
            api_key = 'e6ff482a2f9582991db3cca6'  # Replace with your actual API key
            url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}'

            try:
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200 and data['result'] == 'success':
                    exchange_rate = data['conversion_rate']
                    exchange_rate_decimal = Decimal(str(exchange_rate))
                    converted_amount = amount * exchange_rate_decimal
                    context = {
                        "from_currency": from_currency,
                        "to_currency": to_currency,
                        "exchange_rate": exchange_rate,
                        "original_amount": amount,
                        "converted_amount": converted_amount,
                    }
                    
                    return Response(context, status=status.HTTP_200_OK)
                
                else:
                    context = {
                        "error": "Failed to fetch exchange rate."
                    }
                    
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
            except requests.RequestException:
                context = {
                    "error": "Error connecting to the exchange rate service."
                }
                
                return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Function based View
"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def CategoryListView(request):
    try:
        if request.method == 'GET':
            categories = Category.objects.all()
            serialized_categories = CategorySerializer(categories, many=True)
            context = {
                'message': "Data retrieved successfully",
                'categories': serialized_categories.data
            }
            return Response(context, status=status.HTTP_200_OK)
        
        elif request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    'message': "Category created successfully",
                    'category': serializer.data
                }
                return Response(context, status=status.HTTP_201_CREATED)
            
            else:
                context = {
                    "message": "Invalid data", 
                    "errors": serializer.errors
                }, 
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        context = {
            "message": "An error occurred", 
            "error": str(e)
        }
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)