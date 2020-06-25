import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('src/Multiplication.csv').data
        for row in test_data:
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

    def test_divide_method_calculator(self):
        test_data = CsvReader("src/Division.csv").data
        for row in test_data:
            self.assertEqual(float(row['Result']), self.calculator.divide(row['Value 1'], row['Value 2']))
            self.assertEqual(float(row['Result']), round(self.calculator.result, 9))
        test_data.clear()

    def test_square_root_method_calculator(self):
        test_data = CsvReader('/src/Square_Root.csv').data
        for row in test_data:
            self.assertEqual(round(float(row['Result']), 8), self.calculator.sqrt(row['Value 1']))
            self.assertEqual(round(float(row['Result']), 8), round(self.calculator.result, 8))
        test_data.clear()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
