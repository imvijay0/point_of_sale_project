from django.urls import path
from .views import  MenuItemView, OrderView, LocationView

urlpatterns = [
    path('locations/',LocationView.as_view(), name='locations'),
    path('login/', LocationView.as_view(), name='location-login'),
    
    path('menu-items/', MenuItemView.as_view(), name='menu-items-list'),
    path('menu-items/<int:item_id>/', MenuItemView.as_view(), name='menu-items-detail'),
    
    path('orders/', OrderView.as_view(), name='orders'),
]