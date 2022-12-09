from rest_framework import serializers
from .models import Mailing


class MailingSerializer(serializers.HyperlinkedModelSerializer):
    start_date = serializers.DateTimeField()
    properties_filter = serializers.JSONField()
    end_date = serializers.DateTimeField()
    class Meta:
        model = Mailing
        fields = ['id', 'start_date', 'msg_text', 'properties_filter', 'end_date']

