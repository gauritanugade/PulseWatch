from rest_framework.response import Response


def success_response(
    data=None,
    message="Success",
    status_code=200,
):
    """
    Standard Success Response
    """

    return Response(
        {
            "success": True,
            "status_code": status_code,
            "message": message,
            "data": data,
            "errors": None,
        },
        status=status_code,
    )


def error_response(
    message="Request failed.",
    errors=None,
    status_code=400,
):
    """
    Standard Error Response
    """

    return Response(
        {
            "success": False,
            "status_code": status_code,
            "message": message,
            "data": None,
            "errors": errors,
        },
        status=status_code,
    )