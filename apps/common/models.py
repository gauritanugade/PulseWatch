import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    class Meta:
        abstract = True



