from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email']

    def validate(self, data):
        if not data.get('first_name'):
            raise serializers.ValidationError({"first_name": "Это поле обязательно для заполнения."})
        if not data.get('email'):
            raise serializers.ValidationError({"email": "Это поле обязательно для заполнения."})
        return data


class UserCreateMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']

    def validate(self, data):
        if not data.get('phone_number'):
            raise serializers.ValidationError({"phone_number": "Это поле обязательно для заполнения."})
        return data


class UserCreateWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'middle_name', 'date_of_birth', 'passport_number', 'place_of_birth',
                  'phone_number', 'registration_address']

    def validate(self, data):
        required_fields = ['last_name', 'first_name', 'middle_name', 'date_of_birth', 'passport_number',
                           'place_of_birth', 'phone_number', 'registration_address']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"Это поле обязательно для заполнения."})
        return data
