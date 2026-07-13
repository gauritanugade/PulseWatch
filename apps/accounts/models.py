from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel

from .managers import UserManager


class User(BaseModel, AbstractUser):
    username = None

    full_name = models.CharField(
        max_length=255,
    )

    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "full_name",
    ]

    objects = UserManager()

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email