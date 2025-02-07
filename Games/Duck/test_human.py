import pytest

from human import Human, Foto, Gun
from lake import Lake


class TestHuman:

    @pytest.fixture
    def human(self):
        lake = Lake(5, False)
        return Human(lake)

    def test_update(self, human):
        assert human.getDescription() == "I'm human"


class TestFoto:

    @pytest.fixture
    def foto(self):
        lake = Lake(5, False)
        return Foto(lake, Human(lake))

    def test_update(self, foto):
        assert foto.getDescription() == "I'm human, foto"


class TestGun:

    @pytest.fixture
    def gun(self):
        lake = Lake(5, False)
        return Gun(lake, Human(lake))

    def test_update(self, gun):
        assert gun.getDescription() == "I'm human, gun"
