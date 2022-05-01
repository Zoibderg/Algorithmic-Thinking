# Problem 1: Unique Snowflakes

## The Problem:
We're given a collection of snowflakes, and we hae to determine whether any of the snowflakes in the collection are identical.

A snowflake is represented by six integers, where each integer gives the lenght of one of the snowflakes arms. 

For example, this is a snowflake:\
`[3, 9, 15, 2, 1, 10]`

Two clearly identical snowflakes:\
`[1, 2, 3, 4, 5, 6]`\
`[1, 2, 3, 4, 5, 6]`

Two less-clearly identical snowflakes:\
`[1, 2, 3, 4, 5, 6]`\
`[4, 5, 6, 1, 2, 3]`

We can think of each snowlfakes as a circle. These two snowflakes are identical because we can choose a starting point for the second snowflake and follow it to the right to get the first snowflake. 

Third example snowflakes:\
`[1, 2, 3, 4, 5, 6]`\
`[3, 2, 1, 6, 5, 4]`

If we start with the 1 in the second snowflake and move right (wrapping around to the left), we would get `[1, 6, 5, 4, 3, 2]`, which is not even close to our first snowflake.\
However, if we begin at the 1 in the second snowflake and move left instead, then we get exactly `[1, 2, 3, 4, 5, 6]`

Putting everything together we can conclude that two snowflakes are identical if:
- they are the same
- we can make them the same by moving left through one of the snowflakes
- we can make them the same by moving right through one of the snowflakes

## Input
The first line of input is an integer *n*, which give the number of snowflakes that we'll be processing. The value *n* will be between 1 and 100,000. Each of the following *n* lines represents one snowflake: each line has six integers, where each integer is a leat zero and at most 10,000,000.

## Output
Our output will be the following:
- If identical snowflakes are found print:
  `"{total number of twins} unique snowflakes found:\n[{snowflake1} -> {snowflake2}]"` etc..
- If no identical snowflakes are found print:
  `"no unique twin snowflakes found"`