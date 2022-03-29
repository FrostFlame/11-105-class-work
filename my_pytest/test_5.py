import pytest

from my_pytest.test_3 import Task

# @pytest.mark.smoke
def test_task_equality():
    t1 = Task('sit there', 'brian')
    t2 = Task('do something', 'okken')

    assert t1 == t2


# @pytest.mark.smoke
# @pytest.mark.get
# @pytest.mark.skip('skipped')
# @pytest.mark.skipif(5<2, reason='asdsada')
def test_dict_equality():
    t1_dict = Task('make sandwitch', 'okken')._asdict()
    t2_dict = Task('make sandwitch', 'okkem')._asdict()
    assert t1_dict == t2_dict

@pytest.mark.xfail
def test_fail():
    assert 'a' == 'b'


class TestFoo:
    def test_a(self):
        assert 4 == 4

    def test_b(self):
        assert 4 == 5