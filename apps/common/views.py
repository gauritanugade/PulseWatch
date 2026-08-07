from rest_framework.views import APIView

from .responses import success_response


class HealthAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return success_response(
            message="Application is healthy.",
            data={
                "application": "PulseWatch",
                "status": "UP",
                "version": "1.0.0",
            },
        )