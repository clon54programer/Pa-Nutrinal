from django.http import JsonResponse
from enum import Enum
# from django.core.serializers import serialize


class StatusResponse(Enum):
    """
    Es un enum que contiene los estado
    de una peticion jsonn.
    """
    VALID = 0
    INVALID = -1

    def __str__(self) -> str:
        if self.value == 0:
            return "valid"

        return "invalid"


def ReponseJson(code_http: int, status: StatusResponse, json_body: dict[str, str]) -> JsonResponse:
    data = {
        "status": status.__str__(),
        "code": code_http,
        "data": json_body
    }

    return JsonResponse(data=data)


def ReponseJsonError(error: str, details: str, code_http: int = 400):
    data = {
        "status": StatusResponse.INVALID.__str__(),
        "code": code_http,
        "data": {
            "error": error,
            "details": details
        }
    }

    return JsonResponse(data=data, status=code_http)
