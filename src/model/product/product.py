

class Product:
    """
    Es una clase generica para representar los productos
    de nutrinal

    TODO: Integrar los modelos de Django a la clase.

    Atributos
    ---------
    
    __name_product: str
        Es una cadena que almacena el nombre de un producto
    
    __code: int
        Es un numero entero que identifica el producto.
        Su funcion es facilitar la busqueda de un produto.
    
    __price: int
        Es un numero entero que hace referencia al valor del producto.



"""

    def __init__(self, name_product: str = "",  code: int = 0, price: int = 0):
        # Este mienbro privado debe ser definido
        # por la clase derivada
        self.__name_product = name_product
        # Este mienbro privado debe ser definido
        # por la clase derivada
        self.__code = code
        # Este mienbro privado debe ser definido
        # por la clase derivada
        self.__price = price

    def print(self) -> None:

        print(
            f"Nombre: {self.get_name_product()} Codigo: {self.get_code()} Precio: {self.get_price()}")

    def get_name_product(self) -> str:
        return self.__name_product

    def get_code(self) -> int:
        return self.__code

    def get_price(self) -> int:
        return self.__price
