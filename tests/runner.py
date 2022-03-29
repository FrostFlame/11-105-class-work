import unittest

from tests import test_calc
from tests.test_calc import CalcBasicTest, CalcExTest

calc_test_suite = unittest.TestSuite()
# calc_test_suite.addTest(unittest.makeSuite(CalcBasicTest))
# calc_test_suite.addTest(unittest.makeSuite(CalcExTest))
# calc_test_suite.addTest(CalcBasicTest('test_add'))
# calc_test_suite.addTest(CalcExTest('test_pow'))


# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(calc_test_suite)

test_cases = []
test_cases.append(CalcBasicTest)
test_cases.append(CalcExTest)

test_load = unittest.TestLoader()

suites = []
for tc in test_cases:
    suites.append(test_load.loadTestsFromTestCase(tc))

# suites.append(test_load.loadTestsFromModule(test_calc))
# suites.append(test_load.loadTestsFromModule(test_calc2))
# suites.append(test_load.loadTestsFromModule(test_calc3))
# suites.append(test_load.loadTestsFromName('tests.test_calc'))
# suites.append(test_load.loadTestsFromName('tests.test_calc2'))
# suites.append(test_load.loadTestsFromName('tests.test_calc3'))

res_suite = unittest.TestSuite(suites)

# test_result = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=2)
test_result = runner.run(res_suite)

print("errors")
print(len(test_result.errors))
print("f")
print(len(test_result.failures))