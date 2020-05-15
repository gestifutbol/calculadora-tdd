import unittest
from calculadora import Calculadora


class TestCaseCalculadora(unittest.TestCase):

    def test_initial_value(self):
        calc = Calculadora()
        self.assertEqual(0, calc.value)

