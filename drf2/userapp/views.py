from django.shortcuts import render
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from userapp.serializers import RegistrationSerializers
from rest_framework.authtoken.models import Token
from userapp import signals
# Create your views here.

class RegistrationView(APIView):
    def post(self,request):
        data={}
        serializer = RegistrationSerializers(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Registration Successful"
            data["username"] = account.username
            data["email"]=account.email
            token = Token.objects.get(user=account).key
            data["token"] = token # it will generate a token when user will register
        else:
            data = serializer.errors
        return Response(data)
    
    
    
class LogOutView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)