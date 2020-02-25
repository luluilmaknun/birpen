from django.apps import apps
from django.test import TestCase
from rest_framework.test import APIClient
from pengumuman.apps import PengumumanConfig

from .models import Pengumuman, User

class LandingPageConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(PengumumanConfig.name, 'pengumuman')
        self.assertEqual(apps.get_app_config('pengumuman').name, 'pengumuman')


class LandingPageApiTest(TestCase):
    def test_get_pengumuman(self):
        client = APIClient()
        response = client.get('/api/pengumuman/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], "pengumuman placeholder message")

class filter_test(TestCase):
    def setUp(self):
        user_1 = User(name='athallah.annafis',email='athallah.annafis@ui.ac.id',pwd='kolakdurian')
        user_2 = User(name='ahmad.fauzan',email='ahmad.fauzan@ui.ac.id',pwd='gilarocklo')
        
        pengumuman_1 = Pengumuman(
            oleh=user_2
            matakuliah='PBK'
            jenis=''
            dosen='dr. Lulu Ilma, S.kim'
            ruang='A.12DO'
            sesi='11.00-13.30'
            status='terlambat'
            komentar='terdapat kecelakaan yang membuat macet jalanan '
            tanggal='10.23:12/1/2020'
        )
        pengumuman_2 = Pengumuman(
            oleh=user_1
            matakuliah='DSA'
            jenis=''
            dosen='dr. Nida, S.Kpal'
            ruang='A.12DO'
            sesi='08.00-10.30'
            status='dibatalkan'
            komentar='ada meeting dengan pak presiden'
            tanggal='18.00:13/1/2020'
        )
    
    def test_filter_no_result():
        response = Client().get('/api/pengumuman/?date=12-2-2020')
        response_content = response.content.decode('UTF-8')
		self.assertIn('Tidak ada pengumuman untuk tanggan 12 Februari 2020', response_content)
    
    def test_filter_with_result():
        response = Client.get('/api/pengumuman/?date=13-1-2020')
        response_content = response.content.decode('UTF-8')
        self.assertIn('DSA', response_content)
        self.assertIn('athallah annafis', response_content)
