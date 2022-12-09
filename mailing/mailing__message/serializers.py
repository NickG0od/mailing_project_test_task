from rest_framework import serializers
from .models import Message
from mailing__mailing.models import Mailing
from mailing__client.models import Client


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    mailing = serializers.SlugRelatedField(queryset=Mailing.objects.all(), slug_field='id')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='id')
    class Meta:
        model = Message
        fields = ['id', 'sending_date', 'sending_status', 'mailing', 'client']

