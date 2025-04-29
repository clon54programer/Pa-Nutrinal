from django.http import JsonResponse
from enum import Enum

class StatusResponse(Enum):
    """
    Es un enum que contiene los estado
    de una peticion jsonn.
    """
    VALID = 0
    INVALID = -1

class ResponseJson:
    """
    Es una clase para especificar una forma de
    enviar una respuesta en formato json.
    """
    

    def __init__(self,status: StatusResponse, data: dict[str,str]) -> None:
        self.json_reponse = JsonResponse(data={"status":status,"data":data})
        pass

    def get_reponse(self):
        return self.json_reponse