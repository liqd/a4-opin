from django.db.models.functions import Lower
from rest_framework import serializers

from adhocracy4.projects.models import Project
from euth.users.serializers import UserWithMailSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'participants', 'moderators')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['moderators'].allow_empty = True
        self.fields['participants'].allow_empty = True

    def to_representation(self, instance):
        data = super().to_representation(instance)
        moderators = UserWithMailSerializer(
            instance=instance.moderators.order_by(Lower('username')).all(),
            many=True,
            allow_empty=True,
        )
        participants = UserWithMailSerializer(
            instance=instance.participants.order_by(Lower('username')).all(),
            many=True,
            allow_empty=True,
        )
        data['moderators'] = moderators.data
        data['participants'] = participants.data

        return data
