from django.urls import path
from .views import add_item, get_items, lol

urlpatterns = [
    path('add-item/', add_item, name='add-item'),
    path('get-items/', get_items, name='get-items'),
    path('lol/', lol, name='lol'),
]