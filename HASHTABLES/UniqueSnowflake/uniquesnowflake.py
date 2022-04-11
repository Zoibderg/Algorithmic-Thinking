import itertools
from snowflake import Snowflake

class UniqueSnowflake:
    """
    A class for identifying unique snowflakes.
    """

    def identical_right(self, flake2: Snowflake, start=0) -> bool:
        """
        Determine if 2 snowflakes are identical clockwise.
        """
        flake1 = self
        for i, j in itertools.product(range(flake1.n), range(flake2.n)):
            if flake1.values[i] == flake2.values[j]:  # find matching integers in snowflakes
                offset = j
                while start < flake2.n:  
                    # matching integers found, check entire snowflakes
                    if offset >= flake1.n:  # edgecase
                        offset -= flake1.n
                    elif flake1.values[offset] != flake2.values[start]:  
                        # if any values in either snowflake don't match, return False
                        return False
                    else:
                        # increment pointers
                        start += 1
                        offset += 1
                return True
        return False # edgecase

    def identical_left(self, flake2: Snowflake) -> bool:
        """
        Determine if 2 snowflakes are identical counter-clockwise.
        """
        flake1 = self
        start = flake1.n -1  # start pointer at end of snowflake
        for i, j in itertools.product(range(flake1.n), range(flake2.n)):
            if flake1.values[i] == flake2.values[j]:  # find matching integers in snowflakes
                offset = j - 1
                while start >= 0:
                    # matching integers found, check entire snowflakes
                    if offset < 0:
                        offset += flake1.n
                    elif flake1.values[offset] != flake2.values[start]:
                        # if any values in any snowflake don't match, return false
                        return False
                    else:
                        # increment counters
                        start -= 1
                        offset -= 1
                return True
        return False  # edge case


    def are_identical(self, flake2: Snowflake) -> bool:
        """
        Check if 2 snowflakes are identical, both clockwise and counter-clockwise.
        """
        flake1 = self
        return (UniqueSnowflake.identical_right(flake1, flake2) == 
        UniqueSnowflake.identical_left(flake1, flake2))

if __name__ == '__main__':
    Snowflake = Snowflake([1, 2, 3, 4, 5, 6])