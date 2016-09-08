from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from euth.ratings import models as rating_models

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    child_comments = serializers.SerializerMethodField()
    is_deleted = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        read_only_fields = ('modified', 'created', 'id',
                            'user_name', 'ratings')
        exclude = ('user', 'is_censored', 'is_removed')

    def get_user_name(self, obj):
        """
        Don't show username if comment is marked removed or censored
        """
        if(obj.is_censored or obj.is_removed):
            return 'unknown user'
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
        serializer = CommentSerializer(
            children,
            many=True,
            context={'request': self.context['request']})
        return serializer.data

    def get_is_deleted(self, obj):
        """
        Returns true is one of the flags is set
        """
        return (obj.is_censored or obj.is_removed)

    def get_ratings(self, obj):
        """
        Gets positve and negative rating count as well as
        info on the request users rating
        """
        user = self.context['request'].user
        contenttype = ContentType.objects.get_for_model(obj)
        obj_ratings = rating_models.Rating.objects.filter(
            content_type=contenttype, object_pk=obj.pk)
        positive_ratings = obj_ratings.filter(value=1).count()
        negative_ratings = obj_ratings.filter(value=-1).count()
        try:
            user_rating = obj_ratings.get(user=user)
            user_rating_value = user_rating.value
            user_rating_id = user_rating.pk
        except:
            user_rating_value = None
            user_rating_id = None

        result = {
            'positive_ratings': positive_ratings,
            'negative_ratings': negative_ratings,
            'current_user_rating_value': user_rating_value,
            'current_user_rating_id': user_rating_id
        }

        return result
