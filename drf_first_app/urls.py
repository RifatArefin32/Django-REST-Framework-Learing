# urls.py
from django.urls import path
from .views import CurrencyConversionAPIView, CategoryListView

urlpatterns = [
    path('currency-convert/', CurrencyConversionAPIView.as_view(), name='currency-convert'),
    path('categories/', CategoryListView, name='category-list'),
]
