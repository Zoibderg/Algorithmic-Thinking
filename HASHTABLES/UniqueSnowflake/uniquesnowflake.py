from dataclasses import replace
import itertools
import pprint

from sympy import factor_list

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
                while start < flake1.n:
                    # matching integers found, check entire snowflakes
                    if offset == flake2.n:
                        offset -= flake2.n
                    elif flake1.values[start] != flake2.values[offset]:
                        return False
                    offset += 1
                    start += 1
                return True
        return False # edgecase

    def identical_left(self, flake2: Snowflake, start=0) -> bool:
        """
        Determine if 2 snowflakes are identical counter-clockwise.
        """
        flake1 = self
        for i, j in itertools.product(range(flake1.n), range(flake2.n)):
            if flake1.values[i] == flake2.values[j]:  # find matching integers in snowflakes
                offset = j
                while start < flake1.n:
                    if flake1.values[start] != flake2.values[offset]:
                        return False
                    start += 1
                    offset -= 1
                return True
            return False

    def are_identical(self, flake2: Snowflake) -> bool:
        """
        Check if 2 snowflakes are identical, both clockwise and counter-clockwise.
        """
        flake1 = self
        right = UniqueSnowflake.identical_right
        left = UniqueSnowflake.identical_left
        if not right(flake1, flake2):
            if left(flake1, flake2):
                return True
            else:
                return False
        else:
            return True

    def identify_unique_identical_snowflakes(self, n: int) -> str:
        """
        iter though snowflakes
        determine if any snowflakes are identical
        determine if identical snowflakes are unique
        """
        snowflakes = self  # our list of snowflakes
        memo = {}  # storage for unique identical snowflakes
        nonU = []
        check2 = UniqueSnowflake.are_identical

        for i, j in itertools.combinations(snowflakes, 2):
            # check if 2 snowflakes are identical
            if check2(i, j):
                if tuple(i.values) not in memo.keys():
                    memo[tuple(i.values)] = j.values
                else:
                    nonU.append(tuple(i.values))
                    nonU.append(tuple(j.values))

        for i in nonU:
            if i in memo.keys():
                memo.pop(i)

        if memo:
            #print("unique twins found:\n")
            store = []
            for key, value in memo.items():
                store.append(f"{key} -> {value}")
            return store

        # if there are no unique identical snowflakes in memo
        else:
            return "no unique twin snowflakes found"
