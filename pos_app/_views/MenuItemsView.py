from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import MenuItem
from django.shortcuts import get_object_or_404

class MenuItemView(APIView):
    
    def get(self, request, pk=None):
        """Get menu items (all or single)"""
        if pk:
            item = get_object_or_404(MenuItem, pk=pk)
            data = {
                'id': item.id,
                'name': item.name,
                'price': str(item.price),
                'is_available': item.is_available
            }
        else:
            items = MenuItem.objects.all()
            data = [{
                'id': item.id,
                'name': item.name,
                'price': str(item.price),
            } for item in items]
        return Response(data)

    def post(self, request):
        """Add menu item"""
        item = MenuItem.objects.create(
            name=request.data.get('name'),
            price=request.data.get('price'),
            is_available=request.data.get('is_available', True)
        )
        return Response({
            'id': item.id,
            'name': item.name,
            'price': item.price
        }, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """Delete menu item"""
        item = get_object_or_404(MenuItem, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)