from rest_framework import serializers

from .models import DataKaryaAkhir, SuratKaryaAkhir, ProgramStudi, JenisKaryaAkhir


class JenisKaryaAkhirField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class DataKaryaAkhirSerializer(serializers.ModelSerializer):
    jenis_karya_akhir = JenisKaryaAkhirField(read_only=True)
    mahasiswa = serializers.SerializerMethodField('get_mahasiswa_data')

    class Meta:
        model = DataKaryaAkhir
        fields = [
            'mahasiswa',
            'peminatan_mahasiswa',
            'jenis_karya_akhir',
            'sks_diperoleh',
            'pembimbing',
            'pembimbing_pendamping',
            'judul_karya_id',
            'judul_karya_en',
            'ipk'
        ]

    def get_mahasiswa_data(self, data_karya_akhir):
        mahasiswa = data_karya_akhir.mahasiswa
        return {
            'username': mahasiswa.username,
            'nama': mahasiswa.first_name + ' ' + mahasiswa.last_name,
            'npm': mahasiswa.profile.npm,
            'program_studi': mahasiswa.profile.study_program,
            'angkatan': mahasiswa.profile.year_of_entry
        }


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


class JenisKaryaAkhirSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisKaryaAkhir
        fields = ['nama']
