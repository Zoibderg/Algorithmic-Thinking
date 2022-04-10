import unittest
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from snowflake import Snowflake

class TestSnowflake(unittest.TestCase):
    """
    A class for managing our snowflake tests. 
    """

    def test_identify_identicalTrue(self):  # sourcery skip: class-extract-method
        sf = Snowflake([1, 2, 3, 1, 5], 5)
        ii = sf.identify_identical()
        self.assertEqual(ii, "Twin integers found.\n")

    def test_identify_identicalFalse(self):
        sf = Snowflake([1, 2, 3, 4, 5], 5)
        ii = sf.identify_identical()
        self.assertEqual(ii, "No two integers are alike.\n")

if __name__ == '__main__':
    unittest.main()