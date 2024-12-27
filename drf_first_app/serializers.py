from rest_framework import serializers
from .models import Category

class CurrencyConversionSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)

    def validate(self, data):
        # Ensure that the currencies are different
        if data['from_currency'] == data['to_currency']:
            raise serializers.ValidationError("Source and destination currencies must be different.")
        return data


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'