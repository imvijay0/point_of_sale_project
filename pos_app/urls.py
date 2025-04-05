from django.urls import path
from ._views.LocationView import LocationView,LocationDeleteView
from ._views.MenuItemsView import MenuItemView
from ._views.LoginView import LoginView
from ._views.OrdersView import OrderView

urlpatterns = [
    path('locations/', LocationView.as_view()),
    path('locations/<int:pk>/', LocationDeleteView.as_view(),name="delete-location"),
    
    path('login/', LoginView.as_view()),
    
    path('menu-items/', MenuItemView.as_view()),
    path('menu-items/<int:pk>/', MenuItemView.as_view()),
    
    path('orders/', OrderView.as_view())
]