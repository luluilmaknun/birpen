from rest_framework import serializers
from .models import SuratAkademik


class SuratAkademikSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuratAkademik
        fields = ['jenis_dokumen', 'harga_mahasiswa', 'harga_alumni']
