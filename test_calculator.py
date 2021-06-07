import unittest
import calculator


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 3), 7)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(7, 1), 7)

    def test_divide(self):
        self.assertEqual(calculator.divide(28, 4), 7)


if __name__ == '__main__':
    unittest.main()
