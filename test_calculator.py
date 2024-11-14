import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def testadd(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-5,4),-1)

    def testsub(self):
        self.assertEqual(self.calc.subtract(7,2),5)
        self.assertEqual(self.calc.subtract(-2,0),-2)

    def testmultiply(self):
        self.assertEqual(self.calc.multiply(7,0),0)
        self.assertEqual(self.calc.multiply(-2,2),-4)

    def testdivide(self):
        self.assertEqual(self.calc.divide(5,0),"Cannot divide by zero")
        self.assertEqual(self.calc.divide(-6,2),-3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)

    # Add the following test methods to the TestCalculator class:

if __name == '__main':
    unittest.main()
