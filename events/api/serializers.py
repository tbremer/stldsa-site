from events.models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ("uuid", "title", "start", "url", "status")
