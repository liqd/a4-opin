from rest_framework import serializers

from .models import Rate


class RateSerializer(serializers.ModelSerializer):
    meta_info = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        read_only_fields = ('id', 'meta_info')
        exclude = ('user', 'modified', 'created')

    def get_meta_info(self, obj):
        user = self.context['request'].user
        return obj.get_meta_info(user)
