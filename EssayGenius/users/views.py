from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer,UserGetSerializer
from .models import CustomUser
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.core import serializers


json_seriaizer = serializers.get_serializer("json")
# from rest_framework import status
# from .forms import SignUpForm



class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

# # Create your views here.
@api_view(['POST',])
def signup(request):
    if request.method == 'POST':
        print(request.data)
        serializer = UserSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            user =serializer.save()
            data["response"] ="Successfully registered a new User"
            # data["email"] = user.email
        else:
            data["errors"]= serializer.errors
        return Response(data)

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class= UserGetSerializer

    def get(self, request):
        
        content = CustomUser.objects.get(email=request.user)
        serializer = UserGetSerializer(content)


        return Response(serializer.data)



