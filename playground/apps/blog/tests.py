from django.core.management import call_command
from django.test import TestCase
import openai

class TestExtensions(TestCase):
    def test_list_signals(self):
        assert openai is not None
        result = call_command("list_signals")
        self.assertEqual('', result)
