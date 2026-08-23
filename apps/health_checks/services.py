# import time

# import requests
# from requests.exceptions import RequestException

# from .models import HealthCheck


# def run_health_check(application):
#     start_time = time.perf_counter()

#     try:
#         response = requests.get(
#             application.base_url,
#             timeout=10,
#         )

#         end_time = time.perf_counter()

#         response_time = int(
#             (end_time - start_time) * 1000
#         )

#         status = (
#             HealthCheck.Status.UP
#             if response.status_code < 400
#             else HealthCheck.Status.DOWN
#         )

#         health_check = HealthCheck.objects.create(
#             application=application,
#             status=status,
#             status_code=response.status_code,
#             response_time=response_time,
#             error_message="",
#         )

#         return health_check

#     except RequestException as exc:
#         end_time = time.perf_counter()

#         response_time = int(
#             (end_time - start_time) * 1000
#         )

#         health_check = HealthCheck.objects.create(
#             application=application,
#             status=HealthCheck.Status.DOWN,
#             status_code=0,
#             response_time=response_time,
#             error_message=str(exc),
#         )

#         return health_check



import time

import requests
from requests.exceptions import RequestException

from .models import HealthCheck


REQUEST_TIMEOUT = 10


def run_health_check(application):
    start_time = time.perf_counter()

    try:
        response = requests.get(
            application.monitoring_url,
            timeout=REQUEST_TIMEOUT,
        )

        response_time = int(
            (time.perf_counter() - start_time) * 1000
        )

        if response.status_code < 400:
            status = HealthCheck.Status.UP
            error_message = None
        else:
            status = HealthCheck.Status.DOWN
            error_message = (
                f"HTTP {response.status_code}: "
                f"{response.reason}"
            )

        return HealthCheck.objects.create(
            application=application,
            status=status,
            status_code=response.status_code,
            response_time=response_time,
            error_message=error_message,
        )

    except RequestException as exc:
        response_time = int(
            (time.perf_counter() - start_time) * 1000
        )

        return HealthCheck.objects.create(
            application=application,
            status=HealthCheck.Status.DOWN,
            status_code=0,
            response_time=response_time,
            error_message=str(exc),
        )

from apps.applications.models import Application


def run_application_health_check(application_uuid):
    application = Application.objects.filter(
        uuid=application_uuid,
        deleted_at__isnull=True,
        is_active=True,
    ).first()

    if application is None:
        raise Application.DoesNotExist(
            "Active application not found."
        )

    return run_health_check(application)