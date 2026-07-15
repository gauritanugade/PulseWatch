from rest_framework.views import exception_handler

from apps.common.responses import error_response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return response

    message = "Something went wrong."
    errors = None

    if isinstance(response.data, dict):

        if "detail" in response.data:
            message = str(response.data["detail"])

        else:
            message = "Validation failed."
            errors = response.data

    else:
        errors = response.data

    return error_response(
        message=message,
        errors=errors,
        status_code=response.status_code,
    )