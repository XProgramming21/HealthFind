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



@api_view(['POST'])
def signUpAPIView(request):
    serializer = SignupSerializer(data = request.data)
    if serializer.isValid():


        serializer.save()
        res = { 'status' : status.HTTP_201_CREATED }
        return Response(res, status = status.HTTP_201_CREATED)
    
    res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
    return Response(res, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createAPIPatient(request):
    serializer = createPatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return  Response('true')
    
    return Response(status = status.HTTP_400_BAD_REQUEST)
    




