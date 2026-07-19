from django.shortcuts import get_object_or_404

from .models import Application


def create_application(user, validated_data):
    return Application.objects.create(
        created_by=user,
        **validated_data,
    )


from .models import Application

from apps.common.filters import (
    apply_filters,
    apply_ordering,
    apply_search,
)


def list_applications(request):
    queryset = Application.objects.filter(
        deleted_at__isnull=True,
    )

    queryset = apply_search(
        queryset,
        request,
        search_fields=[
            "name",
            "description",
        ],
    )

    queryset = apply_filters(
        queryset,
        request,
        filter_fields=[
            "environment",
            "is_active",
        ],
    )

    queryset = apply_ordering(
        queryset,
        request,
        allowed_fields=[
            "name",
            "created_at",
        ],
    )

    return queryset

def get_application(uuid):
    return get_object_or_404(
        Application,
        uuid=uuid,
        deleted_at__isnull=True,
    )


def update_application(application, validated_data):
    for key, value in validated_data.items():
        setattr(application, key, value)

    application.save()

    return application


def delete_application(application):
    application.soft_delete()