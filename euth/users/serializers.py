from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'default_avatar')
        read_only_fields = ('id', 'username', 'avatar', 'default_avatar')


# mails should not be exposed in API, so there is a separate one for this
class UserWithMailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'avatar', 'default_avatar', 'email')
        read_only_fields = ('id', 'username', 'avatar', 'default_avatar',
                            'email')
