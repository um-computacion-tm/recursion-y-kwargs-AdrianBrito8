import unittest

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_of_float(self):
        with self.assertRaises(ValueError):
            factorial(2.5)

if __name__ == '__main__':
    unittest.main()

