from collections import OrderedDict

import pytest

from my_pytest.test_3 import Task


# @pytest.mark.run_this_pretty_please
def test_asdict():
    """_asdict() должен возвращать словарь"""
    t_task = Task('do something', 'okken')
    t_dict = t_task._asdict()
    expected = OrderedDict({
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    })
    assert t_dict == expected


def test_replace():
    """Должно заменяться значение"""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
