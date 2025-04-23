

class Client:
    """
    Es una abstracion de un cliente de nutrinal,
    que solo guarda su nombre y sus informacion de contacto.

    TODO: Integrar los modelos de Django a la clase.

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

    __cant_order: int
        Es un numero entero que almacena el numero de compras que 
        ha echo el cliente.
    """

    def __init__(self, name: str, email: str, phone_number: str):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        pass

    def print(self) -> None:
        print(
            f"Name: {self.__name} Phone: {self.__phone_number} Email: {self.__email}")

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_email(self) -> str:
        return self.__email

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        return self.__phone_number


class BuilderClient:

    def __init__(self):
        self.__name = None
        self.__email = None
        self.__phone_number = None

    def build(self):
        return Client(self.__name, self.__email, self.__phone_number)

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number
