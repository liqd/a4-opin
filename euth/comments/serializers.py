from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from euth.rates import models as rate_models

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    child_comments = serializers.SerializerMethodField()
    is_deleted = serializers.SerializerMethodField()
    rates = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        read_only_fields = ('modified', 'created', 'id', 'user_name', 'rates')
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

    def get_rates(self, obj):
        """
        Gets positve and negative rate count as well as
        info on the request users rate
        """
        user = self.context['request'].user
        contenttype = ContentType.objects.get_for_model(obj)
        obj_rates = rate_models.Rate.objects.filter(
            content_type=contenttype, object_pk=obj.pk)
        positive_rates = obj_rates.filter(value=1).count()
        negative_rates = obj_rates.filter(value=-1).count()
        try:
            user_rate = obj_rates.get(user=user)
            user_rate_value = user_rate.value
            user_rate_id = user_rate.pk
        except:
            user_rate_value = None
            user_rate_id = None

        result = {
            'positive_rates': positive_rates,
            'negative_rates': negative_rates,
            'current_user_rate_value': user_rate_value,
            'current_user_rate_id': user_rate_id
        }

        return result
