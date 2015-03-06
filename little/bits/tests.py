from unittest import TestCase
from little.bits import configs
from little.bits.http import do_get, connect

__author__ = 'charlie'


class TestBase(TestCase):

    def test_get(self):
        connect(configs.little_bits_get_url, "GET", None)

    def test_post(self):
        connect(endpoint=configs.little_bits_post_url, method="POST", params='{"percent":100,"duration_ms":5000}')