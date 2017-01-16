from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'default_avatar')
        read_only_fields = ('id', 'username', 'avatar', 'default_avatar')
