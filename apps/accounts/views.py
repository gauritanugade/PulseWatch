from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer
from .services import login_user


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
            return Response(
                {
                    "success": False,
                    "message": "Invalid email or password.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": data,
            },
            status=status.HTTP_200_OK,
        )


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="User Profile",
        description="Get authenticated user profile.",
    )
    def get(self, request):
        return Response(
            {
                "success": True,
                "data": {
                    "uuid": str(request.user.uuid),
                    "email": request.user.email,
                    "full_name": request.user.full_name,
                },
            },
            status=status.HTTP_200_OK,
        )
    
from rest_framework_simplejwt.views import TokenRefreshView


class RefreshAPIView(TokenRefreshView):
    """
    Refresh JWT Access Token
    """
    pass