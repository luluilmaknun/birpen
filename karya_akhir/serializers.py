from rest_framework import serializers

from .models import SuratKaryaAkhir


class SuratKaryaAkhirSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratKaryaAkhir
        fields = ['nama']
