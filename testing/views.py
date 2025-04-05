from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MenuItem
import json

@csrf_exempt  # Temporary for testing
def add_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = MenuItem.objects.create(
                name=data['name'],
                price=data['price']
            )
            return JsonResponse({
                'id': item.id,
                'name': item.name,
                'price': str(item.price)  # Decimal to string
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def get_items(request):
    items = MenuItem.objects.all()
    items_list = [
        {'id': item.id, 'name': item.name, 'price': str(item.price)}
        for item in items
    ]
    return JsonResponse({'items': items_list})

def lol(request):
    return JsonResponse({'message': 'Hello, world!'})