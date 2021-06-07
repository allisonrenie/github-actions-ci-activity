import unittest
import calculator


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 3), 7)


if __name__ == '__main__':
    unittest.main()
