from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from euth.rates import models as rate_models

from .models import Rate


class RateSerializer(serializers.ModelSerializer):
    meta_info = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        read_only_fields = ('id', 'meta_info')
        exclude = ('user', 'modified', 'created')

    def get_meta_info(self, obj):
        user = self.context['request'].user
        related_obj = obj.content_object
        contenttype = ContentType.objects.get_for_model(related_obj)
        pk = related_obj.id
        rates = rate_models.Rate.objects.all().filter(
            content_type=contenttype, object_pk=pk)
        positive_rates_on_same_object = rates.filter(value=1).count()
        negative_rates_on_same_object = rates.filter(value=-1).count()

        try:
            user_rate_on_same_object = rates.get(user=user)
            user_rate_on_same_object_value = user_rate_on_same_object.value
            user_rate_on_same_object_id = user_rate_on_same_object.pk
        except:
            user_rate_on_same_object_value = None
            user_rate_on_same_object_id = None

        result = {
            'positive_rates_on_same_object': positive_rates_on_same_object,
            'negative_rates_on_same_object': negative_rates_on_same_object,
            'user_rate_on_same_object_value': user_rate_on_same_object_value,
            'user_rate_on_same_object_id': user_rate_on_same_object_id
        }

        return result
