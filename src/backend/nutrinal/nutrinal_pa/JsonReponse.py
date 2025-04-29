from django.http import JsonResponse
from enum import Enum
#from django.core.serializers import serialize

class StatusResponse(Enum):
    """
    Es un enum que contiene los estado
    de una peticion jsonn.
    """
    VALID = 0
    INVALID = -1


    def __str__(self) ->  str: 
        if self.value == 0:
            return "valid"

        return "invalid"
        



def ReponseJson(code_http: int, status: StatusResponse, data) -> JsonResponse:
    data = {
        "status":status.__str__(),
        "code": code_http.__str__(),
        "data": data
    }

    return JsonResponse(data=data)