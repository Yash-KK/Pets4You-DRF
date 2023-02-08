from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)
from .permissions import (
    isOwnerPermission
)
#MODELS
from .models import (
    Animal
)

#SERIALIZER
from .serializer import (
    AnimalSerializer
)

# Create your views here.

class AnimalCategories(APIView):
    pass

class AnimalList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        animals = Animal.objects.all().order_by('-created_at')
        serializer = AnimalSerializer(animals, many=True)
        return Response({
            'status': True,
            'message': "Query serialized and now in JSON -> GET",
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data['owner'] = request.user.pk       
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "created animal instance using -> POST",
                'data': serializer.data
            })
        else:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'error': serializer.errors
            })
            
            
class AnimalDetail(APIView):
    permission_classes = [isOwnerPermission]
    def get_object(self,pk):
        try:
            animal = Animal.objects.get(pk=pk)
            return animal
        except:
            raise Http404

    def get(self, request, pk):
        animal = self.get_object(pk)
        animal.increment_views()
        serializer = AnimalSerializer(animal)
        return Response({
            'status': True,
            'message': "detail request using GET",
            'data': serializer.data
        }, status=status.HTTP_200_OK)
        
    
    def patch(self, request, pk):
        animal = self.get_object(pk)
        self.check_object_permissions(request, animal)
        data = request.data
        serializer = AnimalSerializer(animal, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "partially update the instance using -> PATCH",
                'data': serializer.data
            })
        else:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': serializer.errors
            })
    
    def put(self, request, pk):
        data = request.data
        data['owner'] = request.user.pk
        
        animal = self.get_object(pk)
        self.check_object_permissions(request, animal)
        serializer = AnimalSerializer(animal, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "used -> PUT",
                'data': serializer.data
            })
        else:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'error': serializer.errors
            })
    
    def delete(self, request, pk):
        animal = self.get_object(pk)
        self.check_object_permissions(request, animal)
        animal.delete()
        return Response({
            'status': True,
            'message': "animal instance deleted using ->DELETE",
        }, status=status.HTTP_204_NO_CONTENT)
        