from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=8, write_only=True)
#
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'password')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'first_name': {'required': True}, 'last_name': {'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)
