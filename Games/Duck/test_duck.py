import pytest

from duck import RealDuck, RubberDuck, WoodenDuck, FlyPropeller
from pont import Pont


class TestRealDuck:

    @pytest.fixture
    def realduck(self):
        pont = Pont(5, False)
        return RealDuck("blue", "water", pont)

    def test_update(self, realduck):
        assert realduck.color == "blue"
        assert realduck.type == "water"

    def test_performFly(self, realduck):
        assert realduck.performFly() == "I fly"
        realduck.update()
        assert realduck.performFly() == "I swim"

    def test_performQuak(self, realduck):
        assert realduck.performQuack() == "quaaak"


class TestRubberDuck:

    @pytest.fixture
    def rubberduck(self):
        pont = Pont(5, False)
        return RubberDuck("green", "rubber", pont)

    def test_update(self, rubberduck):
        assert rubberduck.color == "green"
        assert rubberduck.type == "rubber"

    def test_performFly(self, rubberduck):
        assert rubberduck.performFly() == "I cannot fly"

    def test_performQuak(self, rubberduck):
        assert rubberduck.performQuack() == "quiiik"


class TestWoodenDuck:

    @pytest.fixture
    def woodenduck(self):
        pont = Pont(5, False)
        return WoodenDuck("brown", "wood", pont)

    def test_update(self, woodenduck):
        assert woodenduck.color == "brown"
        assert woodenduck.type == "wood"

    def test_performFly(self, woodenduck):
        assert woodenduck.performFly() == "I cannot fly"
        woodenduck.setFlyBehavior(FlyPropeller())
        assert woodenduck.performFly() == "I fly with an propeller"

    def test_performQuak(self, woodenduck):
        assert woodenduck.performQuack() == "---"
