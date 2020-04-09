from rest_framework import serializers
from sso_ui.models import AsistenDosen


class AsistenDosenSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsistenDosen
        fields = ['pk', 'username']
