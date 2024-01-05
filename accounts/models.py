from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    pass
