import unittest
import calculator

#Unit tests for functions that return a value.
class Tests (unittest.TestCase):

    def tests_Add(self):
        self.assertEqual(calculator.add(40, 2), 42)
        self.assertEqual(calculator.add(-2, 4), 2)
        self.assertEqual(calculator.add(300, 4000), 4300)
    def tests_Sub(self):
        self.assertEqual(calculator.subtract(40, 2), 38)
        self.assertEqual(calculator.subtract(150, 50), 100)
        self.assertEqual(calculator.subtract(5, 10), -5)
    def tests_Multiply(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.multiply(20, 10), 200)
        self.assertEqual(calculator.multiply(50, 5), 250)
    def tests_Divide(self):
        self.assertEqual(calculator.divide(40, 2), 20)
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(90, 3), 30)
    def tests_Invert(self):
        self.assertEqual(calculator.invert(4), -4)
        self.assertEqual(calculator.invert(-15), 15)
        self.assertEqual(calculator.invert(99), -99)   

if __name__ == '__main__':
    unittest.main()