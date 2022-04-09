class Snowflakes:
    """
    Overall class to manage our snowflakes
    """

    def __init__(self, values: list[int], n: int):
        self.values = values
        self.n = n

    def identify_identical(self) -> str:
        i = 0
        j = i + 1
        found, notfound = "Twin integers found.\n", "No two integers are alike.\n"
        while i < self.n:
            while j < self.n:
                if self.values[i] == self.values[j]:
                    return found
                j += 1
            i += 1
        return notfound

if __name__ == '__main__':
    a = [1, 2, 3, 1, 5]
    SF = Snowflakes(a, 5)
    print(SF.identify_identical())