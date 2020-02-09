from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="landing_page:message-detail")
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')
