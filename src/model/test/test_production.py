from model.production.meat_production import MeatProduction


def test_intance_meat_production():
    intance_one = MeatProduction()
    intance_two = MeatProduction(1)

    assert intance_one is intance_two

    assert intance_two.get_cant() == 1


def test_set_cant_meat_production():
    meat_production = MeatProduction()

    meat_production.set_cant(300)

    assert meat_production.get_cant() == 300

    instance_other = MeatProduction()

    assert instance_other is meat_production
    assert instance_other.get_cant() == meat_production.get_cant()

    print("Cant: "+str(instance_other.get_cant()))
