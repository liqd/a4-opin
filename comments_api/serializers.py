from rest_framework import serializers
from django_comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        read_only_fields = ('submit_date', 'user_name')
        exclude = ('user_email', 'user_url', 'user', 'is_public', 'is_removed', 'ip_address')

    def get_user_name(self, obj):
        return str(obj.user)
