from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response

from .serializers import HealthCheckSerializer
from .services import run_application_health_check


class ManualHealthCheckAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Run Manual Health Check",
        description="Check an application's monitoring URL and save the result.",
        responses=HealthCheckSerializer,
    )
    def post(self, request, uuid):
        health_check = run_application_health_check(uuid)

        return success_response(
            message="Health check completed successfully.",
            data=HealthCheckSerializer(health_check).data,
        )