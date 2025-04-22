from seller import Seller


def test_intance():

    juan = Seller(None)

    juan.set_name("Juan")

    assert juan.get_name() == "Juan"


test_intance()
