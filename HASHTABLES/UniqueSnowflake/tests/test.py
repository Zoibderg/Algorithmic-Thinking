import unittest
import sys
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from snowflake import Snowflake
from uniquesnowflake import UniqueSnowflake


class TestSnowflake(unittest.TestCase):
    """
    A class for managing our snowflake tests.
    """

    def setUp(self):
        self.us = UniqueSnowflake
        self.sf = Snowflake

    def test_identify_identicalTrue(self):  # sourcery skip: class-extract-method
        sf = Snowflake([1, 2, 3, 1, 5])
        ii = sf.identify_identical_integers()

        self.assertEqual(ii, "Twin integers found.\n")

    def test_identify_identicalFalse(self):
        sf = Snowflake([1, 2, 3, 4, 5])
        ii = sf.identify_identical_integers()

        self.assertEqual(ii, "No two integers are alike.\n")

    def test_identify_rightTrue(self):
        sf1 = self.sf([1, 2, 3, 4, 5, 6])
        sf2 = self.sf([4, 5, 6, 1, 2, 3])
        ir = self.us.identical_right(sf1, sf2)

        self.assertEqual(ir, True)

    def test_identify_rightFalse(self):
        sf1 = self.sf([1, 2, 3, 12, 5, 6])
        sf2 = self.sf([4, 5, 6, 1, 2, 3])
        ir = self.us.identical_right(sf1, sf2)

        self.assertEqual(ir, False)

    def test_identify_leftTrue(self):
        sf1 = self.sf([1, 2, 3, 4, 5, 6])
        sf2 = self.sf([3, 2, 1, 6, 5, 4])
        il = self.us.identical_left(sf1, sf2)

        self.assertEqual(il, True)

    def test_identify_leftFalse(self):
        sf1 = self.sf([1, 2, 3, 4, 5, 6])
        sf2 = self.sf([7, 5, 6, 1, 2, 3])
        il = self.us.identical_left(sf1, sf2)
        self.assertEqual(il, False)

    def test_are_identicalTrue(self):
        sf1 = self.sf([1, 2, 3, 4, 5, 6])
        sf2 = self.sf([4, 5, 6, 1, 2, 3])
        ai = self.us.are_identical(sf1, sf2)

        self.assertEqual(ai, True)

    def test_are_identicalFalse(self):
        sf1 = self.sf([1, 2, 3, 12, 5, 6])
        sf2 = self.sf([4, 5, 6, 1, 2, 3])
        ai = self.us.are_identical(sf1, sf2)

        self.assertEqual(ai, False)

    def test_multiple_twins(self):
        sf1, sf2, sf3, sf4 = (self.sf([1, 2, 3, 4, 5, 6]), self.sf([4, 5, 6, 1, 2, 3]),
                            self.sf([7, 8, 9, 1, 2, 3]), self.sf([1, 2, 3, 7, 8, 9]))
        foundput = f"{sf1.values} -> {sf2.values}\n{sf3.values} -> {sf4.values}"

        snowflakes = [sf1, sf2, sf3, sf4]
        iis = self.us.identify_unique_identical_snowflakes(snowflakes, len(snowflakes))
        self.assertEqual(iis, foundput)

    def test_nonuniqueness(self):
        sf1, sf2 = self.sf([1, 2, 3, 4, 5, 6]), self.sf([1, 2, 3, 4, 5, 6])
        sf3, sf4 = self.sf([1, 2, 3, 4, 5, 6]), self.sf([1, 2, 3, 4, 5, 6])
        snowflakes = [sf1, sf2, sf3, sf4]

        iis = self.us.identify_unique_identical_snowflakes(snowflakes, len(snowflakes))
        self.assertEqual(iis, "no unique twin snowflakes found")


if __name__ == '__main__':
    unittest.main()
