

class Production:

    def __init__(self, cant: int = 0, name_product: str = ""):
        self.__cant = cant
        self.__name_product = name_product

    def set_cant(self, cant: int):
        self.__cant = cant

    def get_cant(self) -> int:
        return self.__cant

    def get_name_product(self) -> str:
        return self.__name_product
