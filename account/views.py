from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

#SERIALIZER
from .serializer import (
    RegisterSerializer
)
# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
    
            return Response({
                'status': True,
                'message': "Created a User -> POST",
                'data': serializer.data
            })
@api_view(['POST'])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({
        'status': True,
        'message': "Successfully Logged Out"
    })

