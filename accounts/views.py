from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, GenericAPIView
from rest_framework.views import APIView, View
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserCreationViewSet(GenericAPIView):
    serializer_class = UserCreationSerializer

    def post(self, request):
        print(request.data)
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


