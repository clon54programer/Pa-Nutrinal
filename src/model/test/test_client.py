

def test_instance() -> None:
    juan = Client("juan", "exampe@email", "123455")

    juan.print()


def test_set_and_getter() -> None:
    builder = BuilderClient()
    juan = builder.build()

    # email
    juan.set_email("client@example.com")

    assert juan.get_email() == "client@example.com"

    # phone number
    juan.set_phone_number("312455")

    assert juan.get_phone_number() == "312455"

    # name

    juan.set_name("Juan")

    assert juan.get_name() == "Juan"


test_instance()
test_set_and_getter()
