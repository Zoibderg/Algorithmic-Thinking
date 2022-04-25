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
        if (UniqueSnowflake.identical_right(flake1, flake2) == 
            UniqueSnowflake.identical_left(flake1, flake2)):  # edge case
            # both left and right passed or failed, return either
            return (UniqueSnowflake.identical_left(flake1, flake2) or 
                    UniqueSnowflake.identical_right(flake1, flake2))
        # one case failed, snoflakes cannot match
        else:
            return False

    def identify_identical_snowflakes(self, n: int) -> str:
        """
        TODO: add two edge cases for multiple twins
        if multiple twins are found:
            return all sets of twins
        if a triplit is found:
            return "Non-Uniquie identical snowflakes found"
            snoflakes[i].values -> snoflakes[j].values -> ???
            how will we track this
            what should be the cap?
            i.e. if we get a list of all matching snowflakes except two
            we will only wnat to know the uniquie tiwns. 
        """
        snowflakes = self
        foundput = "Twin snowflakes found:\n"
        twincount = 0
        # set pointers
        i = 0
        j = i + 1  # j should never == i
        while i < n:
            while j < n:
                if UniqueSnowflake.are_identical(snowflakes[i], snowflakes[j]):
                    # idenifed twin snowflakes
                    foundput += f"{snowflakes[i].values} -> {snowflakes[j].values}\n"
                    twincount += 1
                j += 1
            i += 1
        # we have been through all snowflakes
        return foundput if twincount > 0 else "No Twin snoflakes found.\n"