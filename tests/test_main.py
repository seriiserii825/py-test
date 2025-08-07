from tests.src.A import A


def test_main():
    assert 1 == 1


def test_main2():
    x = A.x
    assert x == 2
