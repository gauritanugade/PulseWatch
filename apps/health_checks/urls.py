from django.urls import path

from .views import ManualHealthCheckAPIView


urlpatterns = [
    path(
        "<uuid:uuid>/run/",
        ManualHealthCheckAPIView.as_view(),
        name="manual-health-check",
    ),
]