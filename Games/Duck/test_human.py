import pytest

from hunter import Hunter, Foto, Gun
from pont import Pont


class TestHunter:

    @pytest.fixture
    def hunter(self):
        pont = Pont(5, False)
        return Hunter(pont)

    def test_update(self, hunter):
        assert hunter.getDescription() == "I'm hunter"


class TestFoto:

    @pytest.fixture
    def foto(self):
        pont = Pont(5, False)
        return Foto(pont, Hunter(pont))

    def test_update(self, foto):
        assert foto.getDescription() == "I'm hunter, foto"


class TestGun:

    @pytest.fixture
    def gun(self):
        pont = Pont(5, False)
        return Gun(pont, Hunter(pont))

    def test_update(self, gun):
        assert gun.getDescription() == "I'm hunter, gun"
