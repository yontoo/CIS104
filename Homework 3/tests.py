import unittest
import calculator

class Tests (unittest.TestCase):

    def tests_Add(self):
        self.assertEqual(calculator.add(40, 2), 42)
        self.assertEqual(calculator.add(-2, 4), 2)
        self.assertEqual(calculator.add(300, 4000), 4300)

if __name__ == '__main__':
    unittest.main()