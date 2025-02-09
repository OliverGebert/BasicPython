import pytest

from lake import Lake


class TestLake:

    @pytest.fixture
    def lake(self):
        return Lake(5, 10)

    def test_registerObserver(self, lake):
        for d in range(lake.capacity):
            lake.registerObserver("bird")
            assert lake.count() == d+1
        lake.registerObserver("bird")
        assert lake.count() == lake.capacity
