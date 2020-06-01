from rest_framework import serializers

from .models import SuratKaryaAkhir, ProgramStudi, DataKaryaAkhir


class MahasiswaKaryaAkhirSerializer(serializers.ModelSerializer):
    mahasiswa = serializers.SerializerMethodField('get_mahasiswa_data')

    class Meta:
        model = DataKaryaAkhir
        fields = ['mahasiswa']

    def get_mahasiswa_data(self, data_karya_akhir):
        mahasiswa = data_karya_akhir.mahasiswa
        return {
            'username': mahasiswa.username,
            'nama': mahasiswa.first_name + ' ' + mahasiswa.last_name,
            'npm': mahasiswa.profile.npm,
            'program_studi': mahasiswa.profile.study_program,
            'angkatan': mahasiswa.profile.year_of_entry
        }


class SuratKaryaAkhirSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratKaryaAkhir
        fields = ['nama']


class ProgramStudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramStudi
        fields = ['nama']
