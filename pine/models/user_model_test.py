from django.core.exceptions import ValidationError
from django.test import TestCase
from pine.models import UserModel


class UserModelTest(TestCase):
    def test_valid_user_model_should_be_success(self):
        username = 'test@test.com'
        user = UserModel.objects.create_user(username=username, password='password')
        self.assertEqual(username, str(user))

        # test required internal function
        self.assertEqual(username, user.get_short_name())
        self.assertEqual(username, user.get_full_name())

    def test_invalid_user_model_can_not_be_created(self):
        """Create invalid email should be raise ValidationError
        """
        username = 'ErrorUsername'
        self.assertRaises(ValidationError, UserModel.objects.create_user, username, 'password')
