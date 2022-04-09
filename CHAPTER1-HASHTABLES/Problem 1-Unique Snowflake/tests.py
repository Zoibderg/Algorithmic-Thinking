import unittest


import unittest
from main import Snowflakes

class TestSnowflakes(unittest.TestCase):
    """
    A class for managing our snowflake tests. 
    """

    def test_identify_identicalTrue(self):  # sourcery skip: class-extract-method
        sf = Snowflakes([1, 2, 3, 1, 5], 5)
        ii = sf.identify_identical()
        self.assertEqual(ii, "Twin integers found.\n")

    def test_identify_identicalFalse(self):
        sf = Snowflakes([1, 2, 3, 4, 5], 5)
        ii = sf.identify_identical()
        self.assertEqual(ii, "No two integers are alike.\n")

if __name__ == '__main__':
    unittest.main()