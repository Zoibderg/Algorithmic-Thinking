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
            if flake1.values[i] == flake2.values[j]:  # find 
                offset = j
                while start < flake2.n:
                    if offset >= flake1.n:
                        offset -= flake1.n
                    elif flake1.values[offset] != flake2.values[start]:
                        return False
                    else:
                        start += 1
                        offset += 1
                return True
        return False

    def identical_left(self, flake2: Snowflake) -> bool:
        flake1 = self
        start = flake1.n -1
        for i, j in itertools.product(range(flake1.n), range(flake2.n)):
            if flake1.values[i] == flake2.values[j]:
                offset = j - 1
                while start > 0:
                    if offset < 0:
                        offset += flake1.n
                    elif flake1.values[offset] != flake2.values[start]:
                        return False
                    else:
                        start -= 1
                        offset -= 1
                return True
        return False


    def are_identical(self, flake2: Snowflake) -> bool:
        flake1 = self
        return UniqueSnowflake.identical_right(flake1, flake2) == UniqueSnowflake.identical_left(flake1, flake2)

if __name__ == '__main__':
    US = UniqueSnowflake
    SF1 = Snowflake([1, 2, 3, 4, 5, 6])
    SF2 = Snowflake([4, 5, 6, 1, 2, 3])
    print(US.are_identical(SF1, SF2))