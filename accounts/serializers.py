from rest_framework import serializers
from .models import *


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'middle_name', 'last_name', 'password']
        write_only_fields =('password')