from product.meat import Meat


def test_meat():
    meat = Meat()

    meat.print()

    assert meat.get_name_product() == "Carne de res"

    assert meat.get_price() == 1000
    assert meat.get_code() == 1


test_meat()
