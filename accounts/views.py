from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserCreationViewSet(ModelViewSet):
    serializer_class = UserCreationSerializer
    queryset = UserModel.objects.all()

