import unittest
import lib
class LibTest(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime(2),True)
        self.assertEgual(prime(1),False)
        self.assertEgual(prime(0),False)
        self.assertEgual(prime(14),False)
unittest.main(verbosity=2)     
           
