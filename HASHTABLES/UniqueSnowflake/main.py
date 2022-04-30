import re
import time

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
        with open(file, 'r') as f:
            head = next(f)
            self.n = int(head)
            snowflakes = [line.rstrip('\n') for line in f]
            snowflakes = [[int(i) for i in s.split(' ')] for s in snowflakes]
            snowflakes = [Snowflake(s) for s in snowflakes]
            self.snowflakes = snowflakes

    def findUsnowflakes(self):
        return UniqueSnowflake.identify_unique_identical_snowflakes(self.snowflakes, self.n)
        

if __name__ == '__main__':
    RFlake = ReadSnowflakes()
    RFlake.read_file('./HASHTABLES/UniqueSnowflake/input.txt')
    print(f"Checking {RFlake.n} snowflakes for unique identical twins ...")
    print(f"\n")
    time.sleep(1)
    print(RFlake.findUsnowflakes())