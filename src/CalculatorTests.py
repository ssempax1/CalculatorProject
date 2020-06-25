import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('src/Multiplication.csv').data
        for row in test_data:
            pprint(test_data)
            self.assertEqual(int(row['Result']), self.calculator.multiply(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)
        test_data.clear()

    def test_add_method_calculator(self):
        test_data = CsvReader("src/Addition.csv").data
        for row in test_data:
            self.assertEqual(int(row['Result']), self.calculator.add(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)
        test_data.clear()

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(int(row['Result']), self.calculator.subtract(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)
        test_data.clear()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
