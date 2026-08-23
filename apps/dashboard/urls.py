from django.urls import path

from .views import (
    DashboardApplicationsAPIView,
    DashboardSummaryAPIView,
)


urlpatterns = [
    path(
        "summary/",
        DashboardSummaryAPIView.as_view(),
        name="dashboard-summary",
    ),
    path(
        "applications/",
        DashboardApplicationsAPIView.as_view(),
        name="dashboard-applications",
    ),
]