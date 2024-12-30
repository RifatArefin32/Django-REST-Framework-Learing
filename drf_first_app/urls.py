# urls.py
from django.urls import path
from .views.api import CurrencyConversionAPIView, CategoryListView
from .views.faker import populate_categories

urlpatterns = [
    path('currency-convert/', CurrencyConversionAPIView.as_view(), name='currency-convert'),
    path('categories/', CategoryListView, name='category-list'),
]

fakerurlpatterns = [
    path('populate-categories/', populate_categories, name='populate-category'),
]

urlpatterns += fakerurlpatterns
