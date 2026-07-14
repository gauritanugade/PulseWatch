from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "full_name",
        "role",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "email",
        "full_name",
    )

    ordering = (
        "email",
    )

    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
    )