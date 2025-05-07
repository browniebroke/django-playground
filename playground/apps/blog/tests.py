from django.core.management import call_command
from django.test import TestCase

class TestExtensions(TestCase):
    def test_list_signals(self):
        result = call_command("list_signals")
        self.assertEqual('', result)
