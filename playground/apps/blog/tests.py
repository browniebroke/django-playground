from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

class TestAPIItemsAndProperties(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="jlandercy")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_complete_payload_is_sent(self):
        response = self.client.post(
            "/api/item/",
            data={
                "name": "test",
                "properties": [{"name": "test"}, {"name": "dummy"}],
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content,  b'{"id":1,"properties":[{"name":"test"},{"name":"dummy"}],"name":"test"}')
