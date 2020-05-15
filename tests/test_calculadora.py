import unittest
from calculadora import Calculadora


class TestCaseCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_add_2_and_3(self):
        self.calc.add(2, 3)
        self.assertEqual(5, self.calc.value)

    def test_add_4_and_6(self):
        self.calc.add(4, 6)
        self.assertEqual(10, self.calc.value)

    def test_substract_5_and_6(self):
        self.calc.substract(5, 6)
        self.assertEqual(-1, self.calc.value)

    def test_substract_10_and_5(self):
        self.calc.substract(10, 5)
        self.assertEqual(5, self.calc.value)

    def test_div_6_between_2(self):
        self.calc.div(6, 2)
        self.assertEqual(3, self.calc.value)

    def test_div_8_between_2(self):
        self.calc.div(8, 2)
        self.assertEqual(4, self.calc.value)

    def test_div_between_0_should_launch_zerodivisionerror(self):
        self.assertRaises(ZeroDivisionError, self.calc.div, 5, 0)
