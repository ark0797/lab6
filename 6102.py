import unittest
import lib
class LibTest(unittest.TestCase):
    def test_factorial_nonnegative(self):
        self.assertEqual(lib.factorial(5),120)
        self.assertEqual(lib.factorial(1),1)
        self.assertEqual(lib.factorial(0),1)
    def test_factorial_negative(self):
        self.assertEqual(lib.factyorial(-3),1)
unittest.main(verbosity=2)
