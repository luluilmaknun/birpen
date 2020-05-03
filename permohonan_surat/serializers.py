from rest_framework import serializers

from .models import Pesanan, PesananSuratAkademik

class StatusBayarField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama

class StatusSuratField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama

class SuratAkademikField(serializers.RelatedField):
    def to_representation(self, value):
        return value.jenis_dokumen

class UserField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username

class PesananSuratAkademikSerializer(serializers.ModelSerializer):
    surat_akademik = SuratAkademikField(read_only=True)
    status_surat = StatusSuratField(read_only=True)

    class Meta:
        model = PesananSuratAkademik
        fields = ['surat_akademik', 'status_surat', 'jumlah']

class PesananSerializer(serializers.ModelSerializer):
    pemesan = UserField(read_only=True)
    status_bayar = StatusBayarField(read_only=True)
    pesanan_surat_akademik = serializers.SerializerMethodField(
        'get_pesanan_surat_akademik_by_pesanan')

    class Meta:
        model = Pesanan
        fields = ['pk', 'pemesan', 'nama_pemesan', 'npm_pemesan', 'npm_pemesan', 'waktu_pemesanan',
                  'status_bayar', 'pesanan_surat_akademik']

    def get_pesanan_surat_akademik_by_pesanan(self, pesanan):
        return [PesananSuratAkademikSerializer(psa).data
                for psa in PesananSuratAkademik.objects.filter(pesanan=pesanan)]
