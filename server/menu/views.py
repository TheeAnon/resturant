from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.translation import get_language
from .models import Category, MenuItem
from .serializers import MenuItemSerializer, CategorySerializer

# Gets all category items
@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#get categorised items
@api_view(['GET'])
def categorized_menu_items(request):
    categories = Category.objects.prefetch_related('items')  # Prefetch related items for efficiency
    serialized_data = []
    for category in categories:
        serialized_category = {
            'id': category.id,
            'name': category.name,
            'items': MenuItemSerializer(category.items.all(), many=True).data
        }
        serialized_data.append(serialized_category)
    return Response(serialized_data)

# gets all menu items
@api_view(['GET'])
def menu_items(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# gets one menu items
@api_view(['GET'])
def menu_item(request, pk):
    items = MenuItem.objects.get(pk=pk)
    serializer = MenuItemSerializer(items, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create a category
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create a menu item
@api_view(['POST'])
def create_menu_item(request):
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)