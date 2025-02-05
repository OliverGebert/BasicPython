import pytest

from human import Human, Foto, Gun
from pont import Pont


class TestHuman:

    @pytest.fixture
    def human(self):
        pont = Pont(5, False)
        return Human(pont)

    def test_update(self, human):
        assert human.getDescription() == "I'm human"


class TestFoto:

    @pytest.fixture
    def foto(self):
        pont = Pont(5, False)
        return Foto(pont, Human(pont))

    def test_update(self, foto):
        assert foto.getDescription() == "I'm human, foto"


class TestGun:

    @pytest.fixture
    def gun(self):
        pont = Pont(5, False)
        return Gun(pont, Human(pont))

    def test_update(self, gun):
        assert gun.getDescription() == "I'm human, gun"
