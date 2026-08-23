# from rest_framework import serializers

# from .models import HealthCheck


# class HealthCheckSerializer(serializers.ModelSerializer):
#     application = serializers.CharField(
#         source="application.name",
#         read_only=True,
#     )

#     class Meta:
#         model = HealthCheck

#         fields = (
#             "uuid",
#             "application",
#             "status",
#             "status_code",
#             "response_time",
#             "error_message",
#             "checked_at",
#         )





from rest_framework import serializers

from .models import HealthCheck


class HealthCheckSerializer(serializers.ModelSerializer):
    application_uuid = serializers.UUIDField(
        source="application.uuid",
        read_only=True,
    )

    application_name = serializers.CharField(
        source="application.name",
        read_only=True,
    )

    class Meta:
        model = HealthCheck

        fields = (
            "uuid",
            "application_uuid",
            "application_name",
            "status",
            "status_code",
            "response_time",
            "error_message",
            "checked_at",
        )

        read_only_fields = fields