from rest_framework import serializers
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    child_comments = serializers.SerializerMethodField()
    submit_date = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        read_only_fields = ('submit_date', 'user_name')
        exclude = ('user_email', 'user_url', 'user',
                   'is_public', 'is_removed', 'ip_address')

    def get_user_name(self, obj):
        return str(obj.user)

    def get_child_comments(self, obj):
        content_type = ContentType.objects.get(
            app_label="django_comments", model="comment")
        pk = obj.pk
        children = Comment.objects.all().filter(
            content_type=content_type, object_pk=pk).order_by('submit_date')
        serializer = CommentSerializer(children, many=True)
        return serializer.data

    def get_submit_date(self, obj):
        return obj.submit_date.date()
