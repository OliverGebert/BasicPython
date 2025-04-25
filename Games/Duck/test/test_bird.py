import pytest

from Eco.bird import Duck, Gull, Swan
from Eco.lake import Lake


class TestGull:

    @pytest.fixture
    def gull(self):
        lake = Lake(5, False)
        return Gull(lake)

    def test_update(self, gull):
        assert gull.getDescription() == "Gull"

    def test_move(self, gull):
        assert gull.moveBehavior.move() == "I walk"

    def test_performQuak(self, gull):
        assert gull.performQuack() == "squawk"


class TestDuck:

    @pytest.fixture
    def duck(self):
        lake = Lake(5, False)
        return Duck(lake)

    def test_update(self, duck):
        assert duck.getDescription() == "Duck"

    def test_move(self, duck):
        assert duck.moveBehavior.move() == "I fly"

    def test_performQuak(self, duck):
        assert duck.performQuack() == "quack"


class TestSwan:

    @pytest.fixture
    def swan(self):
        lake = Lake(5, False)
        return Swan(lake)

    def test_update(self, swan):
        assert swan.getDescription() == "Swan"

    def test_move(self, swan):
        assert swan.moveBehavior.move() == "I swim"

    def test_performQuak(self, swan):
        assert swan.performQuack() == "honk"
