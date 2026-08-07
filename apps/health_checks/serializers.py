from rest_framework import serializers

from .models import HealthCheck


class HealthCheckSerializer(serializers.ModelSerializer):
    application = serializers.CharField(
        source="application.name",
        read_only=True,
    )

    class Meta:
        model = HealthCheck

        fields = (
            "uuid",
            "application",
            "status",
            "status_code",
            "response_time",
            "error_message",
            "checked_at",
        )