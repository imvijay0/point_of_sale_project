from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Order, OrderItem
from django.shortcuts import get_object_or_404

class OrderView(APIView):
    def get(self, request):
        """List all orders"""
        orders = Order.objects.all()
        data = []
        for order in orders:
            order_data = {
                'id': order.id,
                'status': order.status,
                'items': [{
                    'item_id': item.menu_item.id,
                    'name': item.menu_item.name,
                    'quantity': item.quantity
                } for item in order.items.all()]
            }
            data.append(order_data)
        return Response(data)

    def post(self, request):
        """Create new order"""
        order = Order.objects.create(
            franchise_location_id=request.data.get('location_id'),
            status='pending'
        )
        
        for item_data in request.data.get('items', []):
            OrderItem.objects.create(
                order=order,
                menu_item_id=item_data.get('item_id'),
                quantity=item_data.get('quantity', 1),
                price_at_order=item_data.get('price')
            )
            
        return Response({
            'order_id': order.id,
            'status': order.status
        }, status=status.HTTP_201_CREATED)