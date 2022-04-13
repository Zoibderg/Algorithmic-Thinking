from snowflake import Snowflake
from uniquesnowflake import UniqueSnowflake

class ReadSnowflakes:
    """
    A class for reading our snowlfake input.
    """

    def __init__(self):
        self.snowflakes = []
        self.n
        self.coutner = 0

        with open('self', 'r') as f:
            for line in f:
                if self.coutner > 0:
                    self.n = int(line)
                else:
                    for integer in line:
                        snowflake = [integer]
                    self.snowflakes.append(snowflake)
                counter += 1
                
