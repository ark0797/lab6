import unittest
import lib
class LibTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome('12321'),True)
        self.assertEqual(palindrome('1221'),True)
        self.assertEqual(palindrome('0'),True)
        self.assetEgual(palindrome(''),True)
unittest.main(verbosity=2)        
