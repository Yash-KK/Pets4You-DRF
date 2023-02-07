from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#MODELS
from .models import (
    Animal
)

#SERIALIZER
from .serializer import (
    AnimalSerializer
)

# Create your views here.
class AnimalList(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response({
            'status': True,
            'message': "Query serialized and now in JSON - GET",
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class AnimalDetail(APIView):
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
            'message': "Detail request using GET",
            'data': serializer.data
        }, status=status.HTTP_200_OK)
        
        
