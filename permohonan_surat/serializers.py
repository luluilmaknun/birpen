from rest_framework import serializers
from permohonan_surat.models import StatusBayar


class StatusBayarSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusBayar
        fields = ['nama']
