import pytest


@pytest.fixture
def get_some_data():
    print('asda')
    yield 42
    print('asdas')


def test_data(get_some_data):
    assert get_some_data == 42
