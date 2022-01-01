from __future__ import unicode_literals
from django.db import models
import uuid
from django.db import models
from django.utils import timezone
from django.db import transaction

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class DataLoggerModel(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password=password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin, DataLoggerModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(UserModel, self).save(*args, **kwargs)
        return self

    # class Meta:
    #     db_table = 'User_basic_information'


class ProfilePicModel(DataLoggerModel):
    image = models.FileField(upload_to='profile/images/', blank=True)


class FriendRequestModel(DataLoggerModel):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='receiver', blank=False)


class FriendModel(DataLoggerModel):
    friends = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='added_friends', blank=False)
