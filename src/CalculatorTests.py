import unittest

from Calculator import Calculator

from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        self.testData = CsvReader('').data

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)
        self.testData = CsvReader('').data


    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        self.testData = CsvReader('Unit_Test_Multiplication.csv').data

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)
        self.testData = CsvReader('Unit_Test_Division.csv').data

    def test_sqr_method_calculator(self):
        self.assertEqual(self.calculator.sqr(2), 4)
        self.assertEqual(self.calculator.result, 4)
        self.testData = CsvReader('Unit_Test_Square.csv').data

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.result, 2)
        self.testData = CsvReader('Unit_Test_Square_Root.csv').data

if __name__ == '__main__':
    unittest.main()
