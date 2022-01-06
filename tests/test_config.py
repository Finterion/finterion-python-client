import os
from unittest import TestCase, mock
from eltyer import Client


class ConfigTest(TestCase):

    def tearDown(self) -> None:
        client = Client()
        client.config.API_KEY = None

    def test_api_key_attribute_setting(self):
        client = Client()
        self.assertIsNone(client.config.API_KEY)
        client.config.API_KEY = "test_key"
        self.assertIsNotNone(client.config.API_KEY)
        self.assertEqual(client.config.API_KEY, "test_key")

    def test_api_key_attribute_setting_from_config(self):
        client = Client()
        self.assertIsNone(client.config.API_KEY)
        client.config.from_dict({"API_KEY": "test_key"})
        self.assertIsNotNone(client.config.API_KEY)
        self.assertEqual(client.config.API_KEY, "test_key")

    @mock.patch.dict(os.environ, {"ELTYER_API_KEY": "test_key"})
    def test_api_key_attribute_setting_from_env(self):
        client = Client()
        self.assertIsNone(client.config.API_KEY)
        client.config.from_env()
        self.assertIsNotNone(client.config.API_KEY)
        self.assertEqual(client.config.API_KEY, "test_key")
