from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response


class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return success_response(
            message="Dashboard fetched successfully.",
            data={},
        )