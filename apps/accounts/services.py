from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken


def login_user(email, password):
    user = authenticate(
        email=email,
        password=password,
    )

    if user is None:
        return None

    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "uuid": str(user.uuid),
            "email": user.email,
            "full_name": user.full_name,
        },
    }


from rest_framework_simplejwt.tokens import RefreshToken


def logout_user(refresh_token):
    token = RefreshToken(refresh_token)
    token.blacklist()