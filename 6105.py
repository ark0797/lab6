import unittest
import lib
import math
class LibTest(unittest.TestCase):
    def test_sin(self):
        self.assertEqual(sin((math.pi)/2),1)
        self.assertEqual(sin(0),0)
        self.assertEqual(sin(2*(math.pi)),0)
unittest.main(verbosity=2)   
        
