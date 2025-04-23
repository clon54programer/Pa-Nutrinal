


class Seller:
    """
    Es una clase que representa a  un
    vendedor de nutrinal.
    
    TODO: Integrar los modelos de Django a la clase.

    Atributos
    ---------

    __name: str
        Es una cadena que almacena el nombre del vendedor.
        NOTE: Esta cadena solo debe almacenar letras.

    __number_sales: int
        Es un numero entero que almacena la cantidad
        de ventas que ha hecho un vendedor.
        
    """

    def __init__(self, name: str):
        self.__name = name

    def set_name(self, name: str) -> None:
        self.__name = name
        pass

    def get_name(self) -> str:
        return self.__name
