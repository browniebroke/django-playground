import csv
import io

import pytest
from django.contrib.auth.models import User
from django.test import TestCase


@pytest.mark.django_db
class TestDownloadCSV:
    def setup_method(self):
        self.user_1 = User.objects.create_user("user1")
        self.user_2 = User.objects.create_user("user2")

    def test_download_status_code(self, client):
        response = client.get("/download-csv/")
        assert response.status_code == 200

    def test_download_content(self, client):
        response = client.get("/download-csv/")
        csv_content = response.getvalue().decode("utf-8")
        csv_reader = csv.reader(io.StringIO(csv_content))
        csv_data = list(csv_reader)
        assert len(csv_data) == 3
        assert csv_data == [['id', 'username'], ['1', 'user1'], ['2', 'user2']]


class TestOtherThing(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("user1")

    def test_single_user_in_db(self):
        users_qs = User.objects.all()
        self.assertEqual(1, len(users_qs))
        self.assertEqual(self.user, users_qs[0])