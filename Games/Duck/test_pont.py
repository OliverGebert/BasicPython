import pytest

from pont import Pont


class TestPont:

    @pytest.fixture
    def pont(self):
        return Pont(5, 10)

    def test_registerObserver(self, pont):
        for d in range(pont.capacity):
            pont.registerObserver("duck")
            assert pont.count() == d+1
        pont.registerObserver("duck")
        assert pont.count() == pont.capacity

    def test_notifyObservers(self, pont):
        pont.setPredator(True)
        assert pont.getPredator()
        pont.setPredator(False)
        assert not pont.getPredator()
