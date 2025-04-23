import production.production as pr
import sys
print(sys.path)


def test_intance_meat_production():
    intance_one = pr.MeatProduction()
    intance_two = pr.MeatProduction(1)

    assert intance_one is intance_two

    assert intance_two.get_cant() == 1


def test_set_cant_meat_production():
    meat_production = pr.MeatProduction()

    meat_production.set_cant(300)

    assert meat_production.get_cant() == 300

    instance_other = pr.MeatProduction()

    assert instance_other is meat_production
    assert instance_other.get_cant() == meat_production.get_cant()

    print("Cant: "+str(instance_other.get_cant()))
