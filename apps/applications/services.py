from django.shortcuts import get_object_or_404

from .models import Application


def create_application(user, validated_data):
    return Application.objects.create(
        created_by=user,
        **validated_data,
    )


def list_applications():
    return Application.objects.filter(
        deleted_at__isnull=True,
    )


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