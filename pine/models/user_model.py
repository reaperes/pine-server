from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Managing user model class.
    You can create user using UserModel.objects.create(\*\*kwargs). But it maybe occur invalid email error.
    You must use **UserModel.objects.create_user(...)** instead of create(...).
    """
    def create_user(self, username, password=None):
        """
        Create and saves a user with the given username (email) and password.
        If username is invalidated email, raise ValidationException

        :param username: user email
        :param password: password

        :raises ValidationException:
            If username(email) is invalid, raise ValidationException.

        :returns UserModel:

        """
        EmailValidator()(username)

        user = self.model(username=username, password=password, is_active=True,
                          last_login=timezone.now())
        user.set_password(password)
        user.save(using=self._db)   # save user to database
        return user


class UserModel(AbstractBaseUser):
    """
    Pine user model. It is used authentication.

    :ivar String username: Unique username. It is user's email.
    :ivar Boolean is_active: user is activation or deactivation. Deactivation user can not login.
    """
    username = models.CharField(verbose_name='username', max_length=254, unique=True,
                                help_text='Required. Max 254 characters. It must be email format string only.',
                                validators=[EmailValidator()])

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """It is used internal django.
        """
        return self.username

    def get_short_name(self):
        """It is used internal django.
        """
        return self.username

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'pine'
