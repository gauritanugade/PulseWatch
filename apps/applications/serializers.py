# from rest_framework import serializers

# from .models import Application


# class CreateApplicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Application
#         fields = (
#             "name",
#             "description",
#             "environment",
#             "is_active",
#         )


# class UpdateApplicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Application
#         fields = (
#             "name",
#             "description",
#             "environment",
#             "is_active",
#         )


# class ApplicationSerializer(serializers.ModelSerializer):
#     created_by = serializers.CharField(source="created_by.email", read_only=True)

#     class Meta:
#         model = Application
#         fields = (
#             "uuid",
#             "name",
#             "description",
#             "environment",
#             "is_active",
#             "created_by",
#             "created_at",
#             "updated_at",
#         )



from rest_framework import serializers

from .models import Application


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "name",
            "description",
            "monitoring_url",
            "environment",
            "is_active",
        )


class UpdateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "name",
            "description",
            "monitoring_url",
            "environment",
            "is_active",
        )


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "uuid",
            "name",
            "description",
            "monitoring_url",
            "environment",
            "is_active",
            "created_at",
            "updated_at",
        )