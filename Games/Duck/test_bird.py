import pytest

from bird import Duck, Gull, Swan, FlyPropeller
from lake import Lake


class TestGull:

    @pytest.fixture
    def realbird(self):
        lake = Lake(5, False)
        return Gull(lake)

    def test_update(self, realbird):
        assert realbird.bird == "Gull"

    def test_performQuak(self, realbird):
        assert realbird.performQuack() == "squawk"


class TestDuck:

    @pytest.fixture
    def rubberbird(self):
        lake = Lake(5, False)
        return Duck(lake)

    def test_update(self, rubberbird):
        assert rubberbird.bird == "Duck"

    def test_performQuak(self, rubberbird):
        assert rubberbird.performQuack() == "quack"


class TestSwan:

    @pytest.fixture
    def woodenbird(self):
        lake = Lake(5, False)
        return Swan(lake)

    def test_update(self, woodenbird):
        assert woodenbird.bird == "Swan"

    def test_performQuak(self, woodenbird):
        assert woodenbird.performQuack() == "honk"
