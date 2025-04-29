from django.http import JsonResponse

class ResponseJson:
    """
    Es una clase para especificar una forma de
    enviar una respuesta en formato json.
    """
    

    def __init__(self,status: str, data: dict[str,str]) -> None:
        self.json_reponse = JsonResponse(data={"status":status,"data":data})
        pass

    def get_reponse(self):
        return self.json_reponse