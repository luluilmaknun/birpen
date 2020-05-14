from rest_framework import serializers

from .models import StatusSurat, StatusBayar
from .models import Pesanan, PesananSuratAkademik, StatusBayar, StatusSurat, \
    SuratAkademik


class StatusBayarField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class StatusSuratField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nama


class SuratAkademikField(serializers.RelatedField):
    def to_representation(self, value):
        return value.jenis_dokumen


class PesananSuratAkademikSerializer(serializers.ModelSerializer):
    surat_akademik = SuratAkademikField(read_only=True)
    status_surat = StatusSuratField(read_only=True)

    class Meta:
        model = PesananSuratAkademik
        fields = ['surat_akademik', 'status_surat', 'jumlah']


class PesananSerializer(serializers.ModelSerializer):
    status_bayar = StatusBayarField(read_only=True)

    class Meta:
        model = Pesanan
        fields = ['pk', 'nama_pemesan', 'npm_pemesan', 'npm_pemesan', 'waktu_pemesanan',
                  'status_bayar']


class DetailPesananSerializer(serializers.ModelSerializer):
    status_bayar = StatusBayarField(read_only=True)
    pesanan_surat_akademik = serializers.SerializerMethodField(
        'get_pesanan_surat_akademik_by_pesanan')

    class Meta:
        model = Pesanan
        fields = ['pk', 'nama_pemesan', 'npm_pemesan', 'npm_pemesan', 'waktu_pemesanan',
                  'status_bayar', 'pesanan_surat_akademik']

    def get_pesanan_surat_akademik_by_pesanan(self, pesanan):
        return [PesananSuratAkademikSerializer(psa).data
                for psa in PesananSuratAkademik.objects.filter(pesanan=pesanan)
                .order_by('surat_akademik__jenis_dokumen')]


class StatusSuratSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusSurat
        fields = ['nama']


class StatusBayarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusBayar
        fields = ['nama']


class SuratAkademikSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuratAkademik
        fields = ['jenis_dokumen', 'harga_mahasiswa', 'harga_alumni']
