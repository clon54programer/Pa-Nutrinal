

"""
    Es una clase que representa a  un
    vendedor de nutrinal
"""


class Seller:

    def __init__(self, name: str):
        self.__name = name

    def set_name(self, name: str) -> None:
        self.__name = name
        pass

    def get_name(self) -> str:
        return self.__name
