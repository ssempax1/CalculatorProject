import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_subtract_method_calculator(self):
        test_data = CsvReader('src/Subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['value 1'], row['value 2']), int(row['result']))
            self.assertEqual(self.calculator.result, int(row['result']))

    def test_add_method_calculator(self):
        test_data = CsvReader('src/Addition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['value 1'], row['value 2']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_multiply_method_calculator(self):
        test_data = CsvReader('src/Multiplication.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['value 1'], row['value 2']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_divide_method_calculator(self):
        test_data = CsvReader('src/Division.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['value 1'], row['value 2']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_sqr_method_calculator(self):
        test_data = CsvReader('src/Square.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.sqr(row['value 1']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_sqrt_method_calculator(self):
        test_data = CsvReader('src/Square_Root.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['value 1']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])


if __name__ == '__main__':
    unittest.main()
