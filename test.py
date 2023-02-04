import unittest

from mymathlib import is_prime

class IsPrimeTests(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_prime(0))
    
    def test_four(self):
        self.assertFalse(is_prime(4))

if __name__ == "__main__":
    unittest.main()
