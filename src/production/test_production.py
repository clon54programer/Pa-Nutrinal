from meat_production import MeatProduction


def test_intance_meat_production():
    intance_one = MeatProduction(0)
    intance_two = MeatProduction(1)

    assert intance_one is intance_two

    assert intance_two.get_cant() == 1


def test_set_cant_meat_production():
    meat_production = MeatProduction(0)

    meat_production.set_cant(300)

    assert meat_production.get_cant() == 300

    instance_other = MeatProduction(0)

    assert instance_other is meat_production
    assert instance_other == 300
