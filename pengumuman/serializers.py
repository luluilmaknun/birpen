from rest_framework import serializers
from .models import Pengumuman

class PembuatField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class NamaMataKuliahField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class JenisPengumumanField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class NamaRuangField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class NamaSesiField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class NamaStatusPengumumanField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class TanggalKelasField(serializers.RelatedField):
    def to_representation(self, value):
        return value.date()


class PengumumanSerializer(serializers.ModelSerializer):
    pembuat = PembuatField(read_only=True)
    nama_mata_kuliah = NamaMataKuliahField(read_only=True)
    jenis_pengumuman = JenisPengumumanField(read_only=True)
    nama_ruang = NamaRuangField(read_only=True)
    nama_sesi = NamaSesiField(read_only=True)
    nama_status_pengumuman = NamaStatusPengumumanField(read_only=True)
    tanggal_kelas = TanggalKelasField(read_only=True)

    class Meta:
        model = Pengumuman
        fields = ['pk', 'created_at', 'modified_at', 'deleted', 'tanggal_kelas', 'pembuat',
                  'nama_mata_kuliah', 'jenis_pengumuman', 'nama_dosen', 'nama_asisten',
                  'nama_ruang', 'nama_sesi', 'nama_status_pengumuman',
                  'komentar']
                  