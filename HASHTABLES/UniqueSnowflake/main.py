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
        self.snowflakes = []  # all stored snoflakes
        self.n = 0  # total amount of snoflakes stored

    def read_file(self, file):
        counter = 0  # counter for tracking line
        with open(file, 'r') as f:
            for line in f:
                if counter <= 0:
                    # first line states total snowflakes in file
                    self.n += int(line)
                else:
                    # after first line, each line represents a snowflake
                    # build snowflake from line
                    snowflake = [int(integer) for integer in line if integer not in ['\n', ' ']]
                    snowflake = Snowflake(snowflake)
                    self.snowflakes.append(snowflake)  # add snowflake to storage
                counter += 1

    def findUsnowflakes(self):
        return UniqueSnowflake.identify_identical_snowflakes(self.snowflakes, self.n)
        

if __name__ == '__main__':
    RFlake = ReadSnowflakes()
    RFlake.read_file('./HASHTABLES/UniqueSnowflake/input.txt')
    print(RFlake.findUsnowflakes())