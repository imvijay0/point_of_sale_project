from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def account_login(request):
    return JsonResponse("Login is success from accounts",safe=False)