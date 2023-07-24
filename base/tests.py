from django.test import TestCase
import requests
from django.http import HttpResponseServerError


class ModelsTestCase(TestCase):
    def test_not_found(self):
        """
        Verify expected status code (HTTP 404 Not Found)
        """
        result = self.client.get("/main_page/j")
        self.assertEqual(result.status_code, 404)