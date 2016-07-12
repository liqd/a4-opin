from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    child_comments = serializers.SerializerMethodField()
    is_deleted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        read_only_fields = ('modified', 'created', 'id', 'user_name')
        exclude = ('user', 'is_censored', 'is_removed')

    def get_user_name(self, obj):
        """
        Don't show username if comment is marked removed or censored
        """
        if(obj.is_censored or obj.is_removed):
            return 'unkonwn user'
        return str(obj.user.username)

    def get_child_comments(self, obj):
        """
        Returns the comments of a comment
        """
        content_type = ContentType.objects.get(
            app_label="comments", model="comment")
        pk = obj.pk
        children = Comment.objects.all().filter(
            content_type=content_type, object_pk=pk).order_by('created')
        serializer = CommentSerializer(children, many=True)
        return serializer.data

    def get_is_deleted(self, obj):
        """
        Returns true is one of the flags is set
        """
        return (obj.is_censored or obj.is_removed)
