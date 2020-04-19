from django.test import TestCase

from rest_framework.test import APIClient


class PlaceholderViewsTest(TestCase):
    def test_get_pengumuman(self):
        client = APIClient()
        response = client.get('/api/alumni/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], "alumni placeholder message")
