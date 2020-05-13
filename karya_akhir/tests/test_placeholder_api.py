from django.test import TestCase

from rest_framework.test import APIClient


class PlaceholderApiTest(TestCase):
    def test_placeholder_api(self):
        client = APIClient()
        response = client.get('/api/karya-akhir/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], "karya akhir placeholder message")
