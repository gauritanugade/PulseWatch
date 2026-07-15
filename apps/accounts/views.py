from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .serializers import LoginSerializer
from .services import login_user

from apps.common.responses import (
    success_response,
    error_response,
)
from .serializers import LogoutSerializer
from .services import logout_user

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Admin Login",
        description="Authenticate admin using email and password.",
        request=LoginSerializer,
        responses={200: None},
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = login_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if data is None:
            return error_response(
                message="Invalid email or password.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return success_response(
            message="Login successful.",
            data=data,
        )

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="User Profile",
        description="Get authenticated user profile.",
    )
    def get(self, request):
       return success_response(
            message="Profile fetched successfully.",
            data={
                "uuid": str(request.user.uuid),
                "email": request.user.email,
                "full_name": request.user.full_name,
            },
        )
    
from rest_framework_simplejwt.views import TokenRefreshView


class RefreshAPIView(TokenRefreshView):

    @extend_schema(
        summary="Refresh Access Token",
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return success_response(
            message="Access token refreshed successfully.",
            data=response.data,
            status_code=response.status_code,
        )


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Logout",
        request=LogoutSerializer,
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        logout_user(
            serializer.validated_data["refresh"],
        )

        return success_response(
            message="Logout successful.",
            status_code=status.HTTP_200_OK,
        )
