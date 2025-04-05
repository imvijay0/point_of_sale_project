from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import FranchiseLocation
from django.shortcuts import get_object_or_404

class LoginView(APIView):
    def post(self, request):
        """Authenticate location"""
        location = get_object_or_404(
            FranchiseLocation, 
            name=request.data.get('name')
        )
        
        if location.password == request.data.get('password'):
            return Response({
                'success': True,
                'location_id': location.id
            })
        
        return Response({
            'success': False,
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)