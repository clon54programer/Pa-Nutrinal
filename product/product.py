

class Product:
    """
Es una clase base para los productos
de nutrinal.
Esta clase solo tiene definiciones de los
mienbros genericos de los productos y sus getters.
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
