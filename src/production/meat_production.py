from production import Production, singleton


@singleton
class MeatProduction(Production):

    def __init__(self, cant: int = 0):
        super().__init__(cant, "Carne de res")
