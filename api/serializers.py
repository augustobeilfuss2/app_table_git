from django.contrib.auth.models import User
from .models import Valores,Registros, Tag
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]



class RegistrosSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Registros
        fields = (
            'id',
            'user',
            'value',
            'date',
            'description',
            'tags'
        )


class TagSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Tag
        fields = (
            'id',
            'user',
            'tags',

        )