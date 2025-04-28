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
    

    Atributos
    ---------

    __name: str
        Es una cadena que almacena el nombre del vendedor.
        NOTE: Esta cadena solo debe almacenar letras.
    _id: str
        Es una cadena que almacena la tarjeta de identificacion del vendedor.
        NOTE: Solo debe almacena numeros enteros.
    _date_joined: DateField
        Es un campo que almacena la fecha de incorporacion del sistema.
        
    """

    name = models.CharField(max_length=100)
    id = models.CharField(max_length=20,unique=True)
    date_joined =  models.DateField(auto_now_add=True)

class Product(models.Model):
    """
    Es una clase generica para representar los productos
    de nutrinal

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
    name_product = models.CharField(max_length=50)
    code = models.CharField(max_length=100,unique=True)
    price = models.DecimalField(max_digits=15,decimal_places=2)

class Production(models.Model):
    """
        Es una clase que representa de un forma simplificada
        la producion de un producto. 

        Atributos
        ---------
        product: llave foranea
            Es una llave foranea que identifica la relacion
            entre el producto y la producion
        
        cant_product: Integer
            Es un numero entero sin signo que almacena la cantidad
            disponible de un producto.    
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    cant_available = models.PositiveIntegerField()



class Order(models.Model):
    """
    Es una representacion de un pedido.

    Atributos
    --------

    __cant_product: int
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

    _product: LLave forana
        Es una llave foranea que identifica los productos que 
        compra el cliente.
    """
    cant_product = models.BigIntegerField(default=0)
    #cant_product = models.IntegerField()
    shipping_destination = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
