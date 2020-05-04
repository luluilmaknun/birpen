from rest_framework import serializers

from .models import StatusSurat


class StatusSuratSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusSurat
        fields = ['nama']
