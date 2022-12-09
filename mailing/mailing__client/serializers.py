from rest_framework import serializers
from .models import Client
from taggit.serializers import (
    TagListSerializerField, TaggitSerializer
)


class ClientSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'mobile_operator_code', 'tags', 'timezone']

