from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import FranchiseLocation, MenuItem, Order, OrderItem
import json

class LocationView(APIView):
    """Handles all location operations"""
    
    def get(self, request):
        """List all locations for dropdown"""
        locations = FranchiseLocation.objects.all().order_by('name')
        data = [{
            'id': loc.id,
            'name': loc.name,
            'address': loc.address
        } for loc in locations]
        return JsonResponse({'locations': data})
    
    def post(self, request):
        """Create new location (admin only)"""
        try:
            data = json.loads(request.body)
            location = FranchiseLocation.objects.create(
                name=data['name'],
                password=data['password'],
                address=data.get('address', '')
            )
            return JsonResponse({
                'success': True,
                'id': location.id,
                'name': location.name
            }, status=201)
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
        
        
class MenuItemView(APIView):
    """Handles menu item operations"""
    def get(self, request):
        """Get all available menu items"""
        items = MenuItem.objects.filter(is_available=True)
        data = [{
            'id': item.id,
            'name': item.name,
            'price': str(item.price),
            'category': item.category.name if item.category else None
        } for item in items]
        return JsonResponse({'menu_items': data})

    def post(self, request):
        """Add new menu item"""
        try:
            data = json.loads(request.body)
            item = MenuItem.objects.create(
                name=data['name'],
                price=data['price'],
                category_id=data.get('category_id'),
                is_available=data.get('is_available', True)
            )
            return JsonResponse({
                'success': True,
                'id': item.id,
                'name': item.name,
                'price': str(item.price),
                'category': item.category.name if item.category else None
            }, status=201)
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    def delete(self, request, item_id):
        """Remove menu item"""
        item = get_object_or_404(MenuItem, id=item_id)
        item.delete()
        return JsonResponse({'success': True})

class OrderView(APIView):
    """Handles order operations"""
    def get(self, request):
        """Get order history"""
        orders = Order.objects.all().order_by('-order_time')
        data = []
        
        for order in orders:
            order_data = {
                'id': order.id,
                'status': order.status,
                'order_time': order.order_time.strftime("%Y-%m-%d %H:%M"),
                'items': [{
                    'name': item.menu_item.name,
                    'quantity': item.quantity,
                    'price': str(item.price_at_order)
                } for item in order.items.all()]
            }
            data.append(order_data)
            
        return JsonResponse({'orders': data})

    def post(self, request):
        """Place new order"""
        try:
            data = json.loads(request.body)
            order = Order.objects.create(
                franchise_location_id=data['location_id'],
                status='pending'
            )
            
            for item in data['items']:
                menu_item = MenuItem.objects.get(id=item['id'])
                OrderItem.objects.create(
                    order=order,
                    menu_item=menu_item,
                    quantity=item['quantity'],
                    price_at_order=menu_item.price
                )
                
            return JsonResponse({
                'success': True,
                'order_id': order.id
            }, status=201)
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)