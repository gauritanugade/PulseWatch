from rest_framework import serializers


class DashboardApplicationsSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    active = serializers.IntegerField()
    inactive = serializers.IntegerField()


class DashboardHealthChecksSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()


class DashboardPerformanceSerializer(serializers.Serializer):
    average_response_time_ms = serializers.FloatField()
    uptime_percentage = serializers.FloatField()


class DashboardSummarySerializer(serializers.Serializer):
    applications = DashboardApplicationsSerializer()
    health_checks = DashboardHealthChecksSerializer()
    performance = DashboardPerformanceSerializer()


class ApplicationHealthSummarySerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    environment = serializers.CharField()
    is_active = serializers.BooleanField()
    total_checks = serializers.IntegerField()
    up_checks = serializers.IntegerField()
    down_checks = serializers.IntegerField()
    uptime_percentage = serializers.FloatField()
    average_response_time_ms = serializers.FloatField()