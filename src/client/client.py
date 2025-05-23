

class Client:
    """
    Es una abstracion de un cliente de nutrinal,
    que solo guarda su nombre y sus informacion de contacto.
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
