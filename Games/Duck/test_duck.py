import pytest

from duck import RealDuck, RubberDuck, WoodenDuck


class TestRealDuck:

    @pytest.fixture
    def realduck(self):
        return RealDuck("blue", "water")

    def test_draw(self, realduck):
        assert "Duck has color blue" in realduck.draw()

    def test_performFly(self, realduck):
        assert realduck.performFly() == "I fly"

    def test_performQuak(self, realduck):
        assert realduck.performQuack() == "quaaak"


class TestRubberDuck:

    @pytest.fixture
    def rubberduck(self):
        return RubberDuck("green", "rubber")

    def test_draw(self, rubberduck):
        assert "Duck has color green" in rubberduck.draw()

    def test_performFly(self, rubberduck):
        assert rubberduck.performFly() == "I cannot fly"

    def test_performQuak(self, rubberduck):
        assert rubberduck.performQuack() == "quiiik"


class TestWoodenDuck:

    @pytest.fixture
    def woodenduck(self):
        return WoodenDuck("brown", "wood")

    def test_draw(self, woodenduck):
        assert "Duck has color brown" in woodenduck.draw()

    def test_performFly(self, woodenduck):
        assert woodenduck.performFly() == "I cannot fly"

    def test_performQuak(self, woodenduck):
        assert woodenduck.performQuack() == "---"
