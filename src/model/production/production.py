

class Production:
    """
        Es una clase que representa de un forma simplificada
        la producion de un producto

        Atributos
        ---------

        __cant: int
            Es un numero entero que almacena la cantidad
            disponible de un producto.
        
        __name_product: str
            Es una cadena que almacena el nombre de un producto.
            NOTE: Esta cadena solo debe almacenar letras.

        __code: int
            Es un numero entero que almacena el codigo de identificacion
            del producto.

    """

    def __init__(self, cant: int = 0, name_product: str = ""):
        self.__cant = cant
        self.__name_product = name_product

    def set_cant(self, cant: int):
        self.__cant = cant

    def get_cant(self) -> int:
        return self.__cant

    def get_name_product(self) -> str:
        return self.__name_product
