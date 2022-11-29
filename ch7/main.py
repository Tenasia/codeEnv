


    
import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def isDivisible(x = 10, y = 5):
        '''is x evenly divisible by y?'''
        return x % y == 0


if __name__ == '__main__':
    unittest.main()