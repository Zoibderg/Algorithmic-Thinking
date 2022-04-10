class Snowflake:
    """
    Overall class to manage our snowflakes
    """

    def __init__(self, values: list[int], n: int):
        self.values = values
        self.n = n

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
    a = [1, 2, 3, 1, 5]
    SF = Snowflake(a, 5)
    print(SF.identify_identical())