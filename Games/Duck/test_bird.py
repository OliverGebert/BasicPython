import pytest

from bird import RealBird, RubberBird, WoodenBird, FlyPropeller
from lake import Lake


class TestRealBird:

    @pytest.fixture
    def realbird(self):
        lake = Lake(5, False)
        return RealBird("blue", "water", lake)

    def test_update(self, realbird):
        assert realbird.color == "blue"
        assert realbird.type == "water"

    def test_performFly(self, realbird):
        assert realbird.performFly() == "I fly"
        realbird.update()
        assert realbird.performFly() == "I swim"

    def test_performQuak(self, realbird):
        assert realbird.performQuack() == "quaaak"


class TestRubberBird:

    @pytest.fixture
    def rubberbird(self):
        lake = Lake(5, False)
        return RubberBird("green", "rubber", lake)

    def test_update(self, rubberbird):
        assert rubberbird.color == "green"
        assert rubberbird.type == "rubber"

    def test_performFly(self, rubberbird):
        assert rubberbird.performFly() == "I cannot fly"

    def test_performQuak(self, rubberbird):
        assert rubberbird.performQuack() == "quiiik"


class TestWoodenBird:

    @pytest.fixture
    def woodenbird(self):
        lake = Lake(5, False)
        return WoodenBird("brown", "wood", lake)

    def test_update(self, woodenbird):
        assert woodenbird.color == "brown"
        assert woodenbird.type == "wood"

    def test_performFly(self, woodenbird):
        assert woodenbird.performFly() == "I cannot fly"
        woodenbird.setFlyBehavior(FlyPropeller())
        assert woodenbird.performFly() == "I fly with an propeller"

    def test_performQuak(self, woodenbird):
        assert woodenbird.performQuack() == "---"
