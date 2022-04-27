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
        flag = False
        for i, j in itertools.product(range(flake1.n), range(flake2.n)):
            if flake1.values[i] == flake2.values[j]:  # find matching integers in snowflakes
                offset = j
                while start < flake2.n:
                    print("right run")
                    print(f"offset: {offset}")
                    print(f"start: {start}")
                    print(flake1.values)
                    print(flake2.values)
                    # matching integers found, check entire snowflakes
                    if flag == False:
                        if offset >= flake1.n:  # edgecase
                            offset -= flake1.n
                    else:
                        if offset < 0 :
                            offset += flake1.n
                    if flake1.values[start] != flake2.values[offset]:  
                        # if any values in either snowflake don't match, return False
                        return False
                    else:
                        # increment pointers
                        if start != flake2.n - 1:
                            if flake1.values[start + 1] == flake2.values[offset - 1]:
                                start += 1
                                offset -= 1
                                flag = True
                            else:
                                start += 1
                                offset += 1
                        else:
                            start += 1
                            offset -= 1
                return True
        return False # edgecase

    def identical_left(self, flake2: Snowflake) -> bool:
        """
        Determine if 2 snowflakes are identical counter-clockwise.
        """
        flake1 = self
        flag = False
        start = 0  # start pointer at end of snowflake
        for i, j in itertools.product(range(flake1.n), range(flake2.n)):
            if flake1.values[i] == flake2.values[j]:  # find matching integers in snowflakes
                offset = j
                jumps = 0
                while jumps < flake1.n:
                    # matching integers found, check entire snowflakes
                    if flag == False:
                        if offset < 0:
                            offset += flake1.n
                    else:
                        if offset >= flake1.n - 1:
                            offset -= flake1.n
                    print("left run")
                    print(f"offset: {offset}")
                    print(f"start: {start}")
                    print(flake1.values)
                    print(flake2.values)
                    print (jumps)
                    print(flag)
                        
                    if flake1.values[start] != flake2.values[offset]:
                        # if any values in any snowflake don't match, return false
                        return False
                    else:
                        # increment counters
                        if offset != flake2.n - 1:
                            if flake1.values[start - 1] == flake2.values[offset + 1]:
                                start -= 1
                                offset += 1
                                flag = True
                                jumps += 1
                            else:
                                start -= 1
                                offset -= 1
                                jumps += 1
                        else:
                            offset -= 1
                            start -= 1
                            jumps += 1
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

    def identify_unique_identical_snowflakes(self, n: int) -> str:
        """
        iter though snowflakes
        determine if any snowflakes are identical
        determine if identical snowflakes are unique
        """
        n = n  # total number of snowflakes
        snowflakes = self  # our list of snowflakes
        memo = {}  # storage for unique identical snowflakes
        overflow = {}  # storage non-unique identical snowflakes
        # iter through list of snowflakes
        for i, j in itertools.product(range(n), range(n)):
            # check if 2 snowflakes are identical
            if i != j and UniqueSnowflake.are_identical(snowflakes[i], snowflakes[j]) == True:
                if (tuple(snowflakes[i].values) not in memo.keys() 
                and snowflakes[i].values not in memo.values()):  # identical snowflakes are unique
                    memo[tuple(snowflakes[i].values)] = snowflakes[j].values
                elif tuple(snowflakes[i].values) in memo:  # identical snowflakes are non-unique
                    overflow[tuple(snowflakes[i].values)] = snowflakes[j].values
                    memo.pop(tuple(snowflakes[i].values))
        # we have been through all snowflakes
        # if there are unique identical snowflakes in memo
        if memo:
            # clean snowflake memo for return
            cleanmemo = pprint.pformat(memo)
            cleanmemo = cleanmemo.strip("{}")
            cleanmemo = cleanmemo.replace(')', ']')
            cleanmemo = cleanmemo.replace('(', '[')
            return f"unique twin snowflakes found:\n{cleanmemo}"
        # if there are no unique identical snowflakes in memo
        else:
            return "no unique twin snowflakes found"
