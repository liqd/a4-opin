from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        read_only_fields = ('description')
        exclude = ('user', 'modified', 'created')
