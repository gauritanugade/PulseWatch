from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginAPIView
from .views import ProfileAPIView
from .views import RefreshAPIView,LogoutAPIView

urlpatterns = [
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),
    path("refresh/", RefreshAPIView.as_view(), name="refresh"),

    path(
        "profile/",
        ProfileAPIView.as_view(),
        name="profile",
    ),

    path("logout/", LogoutAPIView.as_view(), name="logout"),

]
