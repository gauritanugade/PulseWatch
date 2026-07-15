from django.conf import settings
from django.db import models

from apps.common.models import BaseModel


class Application(BaseModel):
    class Environment(models.TextChoices):
        DEVELOPMENT = "development", "Development"
        TESTING = "testing", "Testing"
        STAGING = "staging", "Staging"
        PRODUCTION = "production", "Production"

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    environment = models.CharField(
        max_length=20,
        choices=Environment.choices,
        default=Environment.DEVELOPMENT,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="applications",
    )

    class Meta:
        db_table = "applications"
        ordering = ["-created_at"]
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return self.name