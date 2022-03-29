import unittest

def setUpModule():
    print('module set up')

def tearDownModule():
    print('module tear down')

@unittest.skip('asdsa')
class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('class set up')

    def setUp(self) -> None:
        print('test set up')

    def tearDown(self) -> None:
        print('test tear down')

    @classmethod
    def tearDownClass(cls) -> None:
        print('class tear down')


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

@unittest.skip('asd')
class TestStringMethodas(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('class set up')

    def setUp(self) -> None:
        print('test set up')

    def tearDown(self) -> None:
        print('test tear down')

    @classmethod
    def tearDownClass(cls) -> None:
        print('class tear down')

    @unittest.expectedFailure
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


class NumbersTest(unittest.TestCase):

    def test_even(self):
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
