import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
		calculator = Calculator()
        self.assertIsInstance(calculator,Calculator)


if_name_ =='_main_':
unittest.main()