from rest_framework import serializers
from .models import *


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': False}
        }

    def validated_data(self, data):
        try:
            email = data.get("email", None)
            first_name = data.get("first_name", None)
            last_name = data.get("last_name", None)
            password = data.get("password", None)
            print(serializers.get_error_detail())
            if email:
                if UserModel.objects.filter(email=data["email"]).exists():
                    raise serializers.ValidationError({
                    "Email": "Email is already in use. Try with another email"
                })
            if first_name is None:
                raise serializers.ValidationError(
                    {
                        "first_name": "Enter first name"
                    }
                )
            if last_name is None:
                raise serializers.ValidationError(
                    {
                        "last_name": "Enter last name"
                    }
                )
        except:
            print(serializers.get_error_detail())
        return super.validate(data)

    def create(self, validated_data):
        return Use

