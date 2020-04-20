from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class AlumniSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'is_blocked']
