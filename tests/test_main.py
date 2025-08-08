import pytest
from contextlib import nullcontext as does_not_raise
from main import Calculator


class TestCalculator:
    @pytest.mark.parametrize("x, y, res, expectation", [
        (1, 2, 0.5, does_not_raise()),
        (2, 0, 0, pytest.raises(ZeroDivisionError)),
        (40, '3', 13.333333333333334, pytest.raises(TypeError)),
        (40, None, 0, pytest.raises(TypeError)),
        (40, 3, 13.333333333333334, does_not_raise()),
        (40, -3, -13.333333333333334, does_not_raise()),
        (0, 0, 0, pytest.raises(ZeroDivisionError)),
    ])
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize("x, y, res", [
        (1, 2, 2),
        (2, -4, -8),
        (40, 3, 120),
    ])
    def test_multiply(self, x, y, res):
        assert Calculator().multiply(x, y) == res
