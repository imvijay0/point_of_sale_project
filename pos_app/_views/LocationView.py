from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from ..models import FranchiseLocation
from django.shortcuts import get_object_or_404

class LocationView(APIView):
    def get(self, request):
        """List all locations"""
        locations = FranchiseLocation.objects.all()
        data = [{
            'id': loc.id,
            'name': loc.name,
            'address': loc.address
        } for loc in locations]
        return Response(data)

    def post(self, request):
        """Create new location"""
        location = FranchiseLocation.objects.create(
            name=request.data.get('name'),
            password=request.data.get('password'),
            address=request.data.get('address', '')
        )
        return Response({
            'id': location.id,
            'name': location.name
        }, status=status.HTTP_201_CREATED)


class LocationDeleteView(APIView):
    def delete(self, request, pk):
        "Delete location"
        location = get_object_or_404(FranchiseLocation, pk=pk)
        location.delete()
        return JsonResponse("Location deleted successfully", safe=False)