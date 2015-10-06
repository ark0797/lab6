import unittest
import lib
class LibTest(unittest.TestCase):
    def test_even(self):
        self.assertEqual(lib.even(5),False)
        self.asserEqual(lib.even(13),False)
        self.assertEqual(lib.even(0),True)
        self.assertEqual(lib.even(58),True)
        self.assertEqual(lib.even(-14),True)
unittest.main(verbosity=2)
