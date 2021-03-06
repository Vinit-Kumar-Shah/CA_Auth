from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserList(APIView):

    def get(self, request):
        user1 = User.objects.all()
        serializer = UserSerializer(user1, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer