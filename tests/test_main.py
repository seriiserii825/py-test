import pytest
from main import Calculator


@pytest.mark.parametrize("x, y, res", [
    (1, 2, 0.5),
    (2, -4, -0.5),
    (40, 3, 13.333333333333334),
])
def test_divide(x, y, res):
    assert Calculator().divide(x, y) == res
