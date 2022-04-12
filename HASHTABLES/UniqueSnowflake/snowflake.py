class Snowflake:
    """
    Overall class to manage our snowflakes
    """

    def __init__(self, values: list[int]):
        """
        What defines a snowflake?
        """
        self.values = values  # the length of each snowflake arm
        self.n = len(values)  # the amount of arms the snowflake has/this is limited to 6

    def identify_identical(self) -> str:
        # set pointers
        i = 0
        j = i + 1  # we never want j == i
        # start search
        while i < self.n:
            while j < self.n:
                if self.values[i] == self.values[j]:  # integers are the same
                    return "Twin integers found.\n"
            # increment pointers
                j += 1
            i += 1
        # no like integers found
        return "No two integers are alike.\n"

if __name__ == '__main__':
    SF1 = Snowflake([1, 2, 3, 4, 5, 6])
    SF2 = Snowflake([4, 5, 6, 1, 2, 3])