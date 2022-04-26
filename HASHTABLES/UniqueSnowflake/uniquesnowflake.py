from dataclasses import replace
import itertools
import pprint

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
        if (UniqueSnowflake.identical_right(flake1, flake2) == 
            UniqueSnowflake.identical_left(flake1, flake2)):  # edge case
            # both left and right passed or failed, return either
            return (UniqueSnowflake.identical_left(flake1, flake2) or 
                    UniqueSnowflake.identical_right(flake1, flake2))
        # one case failed, snoflakes cannot match
        else:
            return False

    def identify_identical_snowflakes(self, n: int) -> str:
        n = n
        snowflakes = self
        memo = {}
        overflow = {}
        for i, j in itertools.product(range(n), range(n)):
            if i != j and UniqueSnowflake.are_identical(snowflakes[i], snowflakes[j]) == True:
                if tuple(snowflakes[i].values) not in memo.keys() and snowflakes[i].values not in memo.values():
                    memo[tuple(snowflakes[i].values)] = snowflakes[j].values
                elif tuple(snowflakes[i].values) in memo:
                    overflow[tuple(snowflakes[i].values)] = snowflakes[j].values
                    memo.pop(tuple(snowflakes[i].values))
        # we have been through all snowflakes
        if memo:
            cleanmemo = pprint.pformat(memo)
            cleanmemo = cleanmemo.strip("{}")
            cleanmemo = cleanmemo.replace(')', ']')
            cleanmemo = cleanmemo.replace('(', '[')
            return f"unique twin snowflakes found:\n{cleanmemo}"
        else:
            return "no unique twin snowflakes found"
