from drf_spectacular.utils import extend_schema,OpenApiParameter,OpenApiTypes

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response
from apps.common.pagination import StandardResultsSetPagination
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
        parameters=[
            OpenApiParameter(
                name="page",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Page Number",
            ),
            OpenApiParameter(
                name="page_size",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Records per page",
            ),
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Search by name or description",
            ),
            OpenApiParameter(
                name="environment",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="development/testing/staging/production",
            ),
            OpenApiParameter(
                name="is_active",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="ordering",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="name, -name, created_at, -created_at",
            ),
        ],
        responses=ApplicationSerializer(many=True),
    )
    def get(self, request):
        applications = list_applications(request)

        paginator = StandardResultsSetPagination()

        page = paginator.paginate_queryset(
            applications,
            request,
        )

        serializer = ApplicationSerializer(
            page,
            many=True,
        )

        return paginator.get_paginated_response(
            serializer.data,
            message="Applications fetched successfully.",
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