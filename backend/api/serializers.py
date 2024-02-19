from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from api.models import Patient


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['login', 'password']


class SignupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            validated_data["password"] = make_password(validated_data.get("password"))
            return super(SignupSerializer, self).create(validated_data)
    
    class Meta:
            model = get_user_model()
            fields = ['login','password']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Patient
        fields = '__all__'
    
    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        user = get_user_model().objects.create(**validated_data)
        patient = Patient.objects.create(user=user, **patient_data)

        return patient


