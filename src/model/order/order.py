# FIXME: Provoca un error de inclusion
from product.product import Product


class Order():
    """
    Es una representacion de un pedido.

    Atributos
    --------

    __cant: int
        Es un numero de entero que almacena la cantidad del 
        producto que se debe enviar

    __id_product: int
        Es un numero entero que almacena el codigo que identica
        al producto que se compra.

    __shipping_destination: str
        Es una cadena que almacena la direccion a la cual se debe
        enviar el pedido.

    __seller: LLave foranea
        Sera una llave foranea que hara referencia al vendedor
        que atendio al cliente

    __client: llave foranea
        Es una llave forano que hace referencia al cliente.
        NOTE: Cuando se haga el pedido se debe verificar que
        el cliente este en la base de datos.
    """

    def __init__(self, cant: int = 0, product: Product = None, shipping_destination: str = ""):

        self.__cant = cant
        self.__product = product
        self.__shipping_destination = shipping_destination

        pass
