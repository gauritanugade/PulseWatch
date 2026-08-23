from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response

from .serializers import (
    ApplicationHealthSummarySerializer,
    DashboardSummarySerializer,
)
from .services import (
    get_application_health_summary,
    get_dashboard_summary,
)


class DashboardSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Dashboard Summary",
        description=(
            "Returns overall application, health check, "
            "uptime and performance statistics."
        ),
        responses=DashboardSummarySerializer,
    )
    def get(self, request):
        data = get_dashboard_summary()

        return success_response(
            message="Dashboard summary fetched successfully.",
            data=data,
        )


class DashboardApplicationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Application Health Summary",
        description=(
            "Returns health and performance statistics "
            "for every application."
        ),
        responses=ApplicationHealthSummarySerializer(many=True),
    )
    def get(self, request):
        data = get_application_health_summary()

        return success_response(
            message="Application health summary fetched successfully.",
            data=data,
        )