import unittest
from my_doctest import foo


def setUpModule():
    print('я раньше всех')


def tearDownModule():
    print('Я самый последний')


class TestFoo(unittest.TestCase):
    def test_foo_odd_odd(self):
        self.assertEqual(foo(1, 3), 4)

    def setUp(self):
        print('Я выполняюсь перед каждым тестом')

    def tearDown(self) -> None:
        print('Я выполняюсь после каждого теста')

    @classmethod
    def setUpClass(cls) -> None:
        print('1 раз на весь тесткейс')

    @classmethod
    def tearDownClass(cls) -> None:
        print('1 раз после всего тесткейса')


    my_param_list = [(3, 2, 1), (1, 2, 3), (0, 0, 0)]


    def test_param(self):
        for tup in self.my_param_list:
            with self.subTest():
                self.assertEqual(tup[0], tup[1] + tup[2])


