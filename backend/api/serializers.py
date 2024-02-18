from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['login', 'password']