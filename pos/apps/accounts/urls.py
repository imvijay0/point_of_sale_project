from django.urls import path
from . import views

urlpatterns = [
   
path('account_login/', views.account_login, name='account_login' ),
    
    
]