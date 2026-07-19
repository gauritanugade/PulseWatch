from django.db import models

# Create your models here.
from django.db import models

from apps.applications.models import Application
from apps.common.models import BaseModel


class HealthCheck(BaseModel):
    class Status(models.TextChoices):
        UP = "UP", "UP"
        DOWN = "DOWN", "DOWN"

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="health_checks",
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
    )

    status_code = models.PositiveSmallIntegerField()

    response_time = models.PositiveIntegerField(
        help_text="Response time in milliseconds",
    )

    error_message = models.TextField(
        blank=True,
        null=True,
    )

    checked_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "health_checks"
        ordering = ["-checked_at"]

    def __str__(self):
        return f"{self.application.name} - {self.status}"