from snowflake import Snowflake
from uniquesnowflake import UniqueSnowflake

class ReadSnowflakes:
    """
    A class for reading our snowlfake input.
    """

    def __init__(self):
        self.snowflakes = []
        self.n = 0

    def read_file(self, file):
        counter = 0
        with open(file, 'r') as f:
            for line in f:
                if counter <= 0:
                    self.n = int(line)
                else:
                    snowflake = [int(integer) for integer in line if integer != '\n']
                    snowflake = Snowflake(snowflake)
                    self.snowflakes.append(snowflake)
                counter += 1

    def findUsnowflakes(self):
        return UniqueSnowflake.identify_identical_snowflakes(self.snowflakes, self.n)
        

if __name__ == '__main__':
    RFlake = ReadSnowflakes()
    RFlake.read_file('./HASHTABLES/UniqueSnowflake/input.txt')
    print(RFlake.findUsnowflakes())