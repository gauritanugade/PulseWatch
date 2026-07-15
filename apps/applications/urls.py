from django.urls import path

from .views import (
    ApplicationDetailAPIView,
    ApplicationListCreateAPIView,
)

urlpatterns = [
    path(
        "",
        ApplicationListCreateAPIView.as_view(),
        name="application-list-create",
    ),

    path(
        "<uuid:uuid>/",
        ApplicationDetailAPIView.as_view(),
        name="application-detail",
    ),
]