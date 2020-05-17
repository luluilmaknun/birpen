from rest_framework import serializers

from .models import SuratKaryaAkhir, ProgramStudi


class SuratKaryaAkhirSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratKaryaAkhir
        fields = ['nama']


class ProgramStudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramStudi
        fields = ['nama']
