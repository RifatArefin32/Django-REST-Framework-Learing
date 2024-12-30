# faker_views.py
from faker import Faker
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_first_app.serializers import CategorySerializer
from drf_first_app.models import Category


# Create fake and dummy data
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def populate_categories(request):
    fake = Faker()
    categories = []
    # generate 10 fake categories
    for _ in range(10):  
        category = Category.objects.create(
            category_code=fake.unique.bothify(text="CAT###"),
            name=fake.word().capitalize(),
            description=fake.text(max_nb_chars=200)
        )
        categories.append(category)
    
    serialized_categories = CategorySerializer(categories, many=True)

    return Response({
        'message': 'successfully created data',
        'data': serialized_categories.data
    }, status=status.HTTP_200_OK)