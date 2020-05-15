import unittest
from calculadora import Calculadora


class TestCaseCalculadora(unittest.TestCase):

    def test_initial_value(self):
        calc = Calculadora()
        self.assertEqual(0, calc.value)

    def test_add_2_and_3(self):
        calc = Calculadora()
        calc.add(2, 3)
        self.assertEqual(5, calc.value)

    def test_add_4_and_6(self):
        calc = Calculadora()
        calc.add(4, 6)
        self.assertEqual(10, calc.value)
