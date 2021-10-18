from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class ModelTests(TestCase):
    def test_bob(self):
        self.assertEqual(get_user_model(), User)
