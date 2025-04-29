from django.http import JsonResponse

class ResponseJson:
    

    def __init__(self,status: str, data: dict[str,str]) -> None:
        self.json_reponse = JsonResponse(data={"status":status,"data":data})
        pass

    def get_reponse(self):
        return self.json_reponse