from drf_spectacular.utils import extend_schema

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response

from .serializers import (
    ApplicationSerializer,
    CreateApplicationSerializer,
    UpdateApplicationSerializer,
)

from .services import (
    create_application,
    list_applications,
    get_application,
    update_application,
    delete_application,
)


class ApplicationListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Create Application",
        request=CreateApplicationSerializer,
        responses=ApplicationSerializer,
    )
    def post(self, request):
        serializer = CreateApplicationSerializer(
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)

        application = create_application(
            request.user,
            serializer.validated_data,
        )

        return success_response(
            message="Application created successfully.",
            data=ApplicationSerializer(application).data,
            status_code=201,
        )

    @extend_schema(
        summary="Application List",
        responses=ApplicationSerializer(many=True),
    )
    def get(self, request):
        applications = list_applications()

        return success_response(
            message="Applications fetched successfully.",
            data=ApplicationSerializer(
                applications,
                many=True,
            ).data,
        )


class ApplicationDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Application Detail",
    )
    def get(self, request, uuid):
        application = get_application(uuid)

        return success_response(
            message="Application fetched successfully.",
            data=ApplicationSerializer(application).data,
        )

    @extend_schema(
        summary="Update Application",
        request=UpdateApplicationSerializer,
    )
    def put(self, request, uuid):
        application = get_application(uuid)

        serializer = UpdateApplicationSerializer(
            application,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)

        application = update_application(
            application,
            serializer.validated_data,
        )

        return success_response(
            message="Application updated successfully.",
            data=ApplicationSerializer(application).data,
        )

    @extend_schema(
        summary="Delete Application",
    )
    def delete(self, request, uuid):
        application = get_application(uuid)

        delete_application(application)

        return success_response(
            message="Application deleted successfully.",
        )