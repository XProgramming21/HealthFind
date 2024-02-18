from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from api.serializers import *
from rest_framework import status

# Create your views here.


@api_view(['POST'])
def loginAPIView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        login = serializer.validated_data["login"]
        password = serializer.validated_data["password"]
        user = authenticate(request, login=login, password=password)
        if user:
            token, create = Token.objects.get_or_create(user=user)
            
            response = {
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                        "Token" : token.key,
                        "create": token.created
                        }
                    }
            return Response(response, status = status.HTTP_200_OK)
            
        else:
            return Response('erreur token')
        
    return Response('erer')

