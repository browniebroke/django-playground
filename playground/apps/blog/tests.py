from django.core.validators import URLValidator
from django.test import TestCase

# Create your tests here.
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    url = serializers.URLField()


class TestUrl(TestCase):
    def test_valid_url(self):
        serializer = MySerializer(data={'url': 'http://testserver/path'})
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_url_validator(self):
        validator = URLValidator()
        self.assertIsNone(validator('http://testserver/path'))