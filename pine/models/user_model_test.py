from django.core.exceptions import ValidationError
from django.test import TestCase
from pine.models import UserModel


class UserModelTest(TestCase):
    def test_invalid_user_model_can_not_be_created(self):
        username = 'ErrorUsername'
        self.assertRaises(ValidationError, UserModel.objects.create_user, username, 'password')