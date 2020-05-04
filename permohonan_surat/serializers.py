from rest_framework import serializers

from .models import StatusSurat, StatusBayar


class StatusSuratSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusSurat
        fields = ['nama']


class StatusBayarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusBayar
        fields = ['nama']
