import unittest

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_cero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_uno(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_dos(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_tres(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_diez(self):
        self.assertEqual(fibonacci(10), 55)

if __name__=="__main__":
    unittest.main()