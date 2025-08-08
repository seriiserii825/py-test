import pytest
from main import Calculator


class TestCalculator:
    @pytest.mark.parametrize("x, y, res", [
        (1, 2, 0.5),
        (2, -4, -0.5),
        (40, 3, 13.333333333333334),
    ])
    def test_divide(self, x, y, res):
        assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize("x, y, res", [
        (1, 2, 2),
        (2, -4, -8),
        (40, 3, 120),
    ])
    def test_multiply(self, x, y, res):
        assert Calculator().multiply(x, y) == res
