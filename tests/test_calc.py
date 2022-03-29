import sys
import unittest

import jsonpickle


def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


def pow(a, b):
    return a ** b


def sqrt(a):
    return a ** 0.5



class CalcBasicTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(4, 2), 3)

    def test_div(self):
        self.assertEqual(div(8, 4), 2)

    def test_mul(self):
        self.assertEqual(mul(2, 5), 10)

@unittest.skip("skip class")
class CalcExTest(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(pow(2, 5), 32)

    # @unittest.skipIf(jsonpickle.__version__ < '2.1.0', reason='unsupported lib')
    @unittest.skipUnless(sys.platform.startswith('ubuntu'), reason='requires win')
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)


if __name__ == '__main__':
    unittest.main()