from snowflake import Snowflake
from uniquesnowflake import UniqueSnowflake


class ReadSnowflakes:
    """
    A class for reading our snowlfake input.
    """

    def __init__(self):
        """
        init snowflake storage
        """
        self.snowflakes = None  # all stored snoflakes
        self.n = 0  # total amount of snoflakes stored

    def read_file(self, file):
        """
        read thorough file and build snowflakes
        """
        with open(file, 'r') as f:
            # first line contains total number of snowflakes
            head = next(f)
            self.n = int(head)
            # build snowflakes
            snowflakes = [line.rstrip('\n') for line in f]  # strip new line from lines
            snowflakes = [[int(i) for i in s.split(' ')] for s in snowflakes]  # build snowflakes from integers
            snowflakes = [Snowflake(s) for s in snowflakes]  # set snowflakes as snowflakes
            self.snowflakes = snowflakes

    def findUsnowflakes(self):
        # call to identify unique tiwn snowflakes
        return UniqueSnowflake.identify_unique_identical_snowflakes(self.snowflakes, self.n)


if __name__ == '__main__':
    RFlake = ReadSnowflakes()
    RFlake.read_file('./HASHTABLES/UniqueSnowflake/input.txt')  # read input
    # show prompt of engagement
    print(f"Checking {RFlake.n} snowflakes for unique identical twins ...\n")
    print(RFlake.findUsnowflakes())  # return result
