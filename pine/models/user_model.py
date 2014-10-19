from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        # If email is invalidate, it throws ValidationError
        EmailValidator()(username)

        user = self.model(username=username, password=password, is_active=True,
                          last_login=timezone.now())
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    """
    Pine user. Username is email.
    """
    username = models.CharField(verbose_name='username', max_length=254, unique=True,
                                help_text='Required. Max 254 characters. It must be email format string only.',
                                validators=[EmailValidator()])

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'pine'
