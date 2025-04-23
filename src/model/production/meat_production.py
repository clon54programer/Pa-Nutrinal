# from production import Production
from production import Production


class MeatProduction(Production):

    _instance = None

    def __init__(self, cant: int = 0):
        if not hasattr(self, "_initialized"):
            super().__init__(cant, "Carne de res")
            self._in_initialized = True

    def __new__(cls, cant: int = 0):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
