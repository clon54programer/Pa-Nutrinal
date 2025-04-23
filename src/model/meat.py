from product.product import Product


class Meat(Product):

    def __init__(self):
        super().__init__("Carne de res", 1, 1000)
