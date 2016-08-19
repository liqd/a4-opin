from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        exclude = ('user', 'modified', 'created')

    def validate(self, attrs):

        content_type = attrs.get('content_type')
        object_pk = attrs.get('object_pk')
        user = self.context['request'].user

        try:
            Report.objects.get(
                content_type=content_type, object_pk=object_pk, user=user)
        except Report.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError(
                'user report on this item already exists')
