from django.db.models import Avg, Count, Q

from apps.applications.models import Application
from apps.health_checks.models import HealthCheck


def get_dashboard_summary():
    applications = Application.objects.filter(
        deleted_at__isnull=True,
    )

    health_checks = HealthCheck.objects.filter(
        deleted_at__isnull=True,
    )

    total_applications = applications.count()

    active_applications = applications.filter(
        is_active=True,
    ).count()

    inactive_applications = applications.filter(
        is_active=False,
    ).count()

    total_health_checks = health_checks.count()

    up_checks = health_checks.filter(
        status=HealthCheck.Status.UP,
    ).count()

    down_checks = health_checks.filter(
        status=HealthCheck.Status.DOWN,
    ).count()

    average_response_time = health_checks.aggregate(
        average=Avg("response_time"),
    )["average"]

    uptime_percentage = (
        (up_checks / total_health_checks) * 100
        if total_health_checks
        else 0
    )

    return {
        "applications": {
            "total": total_applications,
            "active": active_applications,
            "inactive": inactive_applications,
        },
        "health_checks": {
            "total": total_health_checks,
            "up": up_checks,
            "down": down_checks,
        },
        "performance": {
            "average_response_time_ms": round(
                average_response_time or 0,
                2,
            ),
            "uptime_percentage": round(
                uptime_percentage,
                2,
            ),
        },
    }


def get_application_health_summary():
    applications = (
        Application.objects
        .filter(deleted_at__isnull=True)
        .annotate(
            total_checks=Count(
                "health_checks",
                filter=Q(
                    health_checks__deleted_at__isnull=True,
                ),
            ),
            up_checks=Count(
                "health_checks",
                filter=Q(
                    health_checks__status=HealthCheck.Status.UP,
                    health_checks__deleted_at__isnull=True,
                ),
            ),
            down_checks=Count(
                "health_checks",
                filter=Q(
                    health_checks__status=HealthCheck.Status.DOWN,
                    health_checks__deleted_at__isnull=True,
                ),
            ),
            average_response_time=Avg(
                "health_checks__response_time",
                filter=Q(
                    health_checks__deleted_at__isnull=True,
                ),
            ),
        )
        .order_by("name")
    )

    result = []

    for application in applications:
        uptime = (
            (application.up_checks / application.total_checks) * 100
            if application.total_checks
            else 0
        )

        result.append(
            {
                "uuid": str(application.uuid),
                "name": application.name,
                "environment": application.environment,
                "is_active": application.is_active,
                "total_checks": application.total_checks,
                "up_checks": application.up_checks,
                "down_checks": application.down_checks,
                "uptime_percentage": round(uptime, 2),
                "average_response_time_ms": round(
                    application.average_response_time or 0,
                    2,
                ),
            }
        )

    return result