from django.db import models

# Create your models here.
class Client(models.Model):
    """
    Es una abstracion de un cliente de nutrinal,
    que solo guarda su nombre y sus informacion de contacto.

    TODO: Crear un metodo o una funcionalidad para poder rastrear los pedidos de un cliente


    Atributos
    ---------

    __name: str
        Es una cadena que almacena un nombre de una persona
        natural o de una organizacion.
    
    __email: str
        Es una cadena que almacena el correo de la persona
        o organizacion.
    
    __phone_number: str
        Es una cadena que almacena un numero de telefono.
        NOTE: Esta cadena solo puede tener numeros en ella.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)


class Seller(models.Model):
    """
    Es una clase que representa a  un
    vendedor de nutrinal.
    
    TODO: Integrar los modelos de Django a la clase.

    Atributos
    ---------

    __name: str
        Es una cadena que almacena el nombre del vendedor.
        NOTE: Esta cadena solo debe almacenar letras.
    _id: str
        Es una cadena que almacena la tarjeta de identificacion del vendedor.
        NOTE: Solo debe almacena numeros enteros.
        
    """



class Order(models.Model):
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
