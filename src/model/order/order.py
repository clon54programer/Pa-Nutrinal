from product.product import Product


class Order():

    def __init__(self, cant: int = 0, product: Product = None, shipping_destination: str = ""):

        self.__cant = cant
        self.__product = product
        self.__shipping_destination = shipping_destination

        pass
