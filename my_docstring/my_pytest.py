import pytest
from my_doctest import foo


def test_foo_odd_odd():
    assert foo(1, 3) == 4


@pytest.fixture
def some_data():
    assert True
    yield 42
    assert True


def test_fixt(some_data):
    assert some_data == 42


my_param_list = [(3, 2, 1), (1, 2, 3), (0, 0, 0)]


@pytest.mark.parametrize('x, y, z', my_param_list)
def test_param(x, y, z):
    assert x == y + z