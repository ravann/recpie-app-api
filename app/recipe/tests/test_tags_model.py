from django.test import TestCase
from django.contrib.auth import get_user_model

from recipe import models as rmodels


def sample_user(email='test@test.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_tag_str(self):
        """Test tag string representation"""
        tag = rmodels.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )
        self.assertEqual(str(tag), tag.name)
