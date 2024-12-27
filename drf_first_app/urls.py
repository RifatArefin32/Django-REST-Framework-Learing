# urls.py
from django.urls import path
from .views import CurrencyConversionAPIView

urlpatterns = [
    path('currency-convert/', CurrencyConversionAPIView.as_view(), name='currency-convert'),
]
