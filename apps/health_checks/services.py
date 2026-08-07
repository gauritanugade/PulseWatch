import time

import requests
from requests.exceptions import RequestException

from .models import HealthCheck


def run_health_check(application):
    start_time = time.perf_counter()

    try:
        response = requests.get(
            application.base_url,
            timeout=10,
        )

        end_time = time.perf_counter()

        response_time = int(
            (end_time - start_time) * 1000
        )

        status = (
            HealthCheck.Status.UP
            if response.status_code < 400
            else HealthCheck.Status.DOWN
        )

        health_check = HealthCheck.objects.create(
            application=application,
            status=status,
            status_code=response.status_code,
            response_time=response_time,
            error_message="",
        )

        return health_check

    except RequestException as exc:
        end_time = time.perf_counter()

        response_time = int(
            (end_time - start_time) * 1000
        )

        health_check = HealthCheck.objects.create(
            application=application,
            status=HealthCheck.Status.DOWN,
            status_code=0,
            response_time=response_time,
            error_message=str(exc),
        )

        return health_check