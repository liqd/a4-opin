from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'avatar_fallback')
        read_only_fields = ('id', 'username', 'avatar', 'avatar_fallback')

    def get_avatar(self, obj):
        if obj.avatar:
            image = get_thumbnailer(obj.avatar)['avatar_small']
            return image.url


# mails should not be exposed in API, so there is a separate one for this
class UserWithMailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'avatar', 'avatar_fallback', 'email')
        read_only_fields = ('id', 'username', 'avatar', 'avatar_fallback',
                            'email')
