** Your Answer **

Number the colors 0, 1, and 2. Arrange the players 0, 1, 2, 3 counterclockwise. Players 0 and 1 calculate L+R-2 (the color of the hat on their left, plus the color of the hat on their right, minus two) while players 2 and 3 calculate L-R; players 0, 2, and 3 guess color 0 if their result is negative, 1 if zero, 2 if positive; player 1 guesses color 2 if their result is negative, 1 if zero, 0 if positive

** Show Your Work **

When I think about problems like this, my first assumption is always "Looking at your fellow players' hats gives you no information about your own hat. Therefore, the problem's impossible." I know that's not true, though -- but I couldn't figure out how to get started on the solution. So, I went to my computer.

After some thought, I realized that there were a total of 3^(3*3*4) > 150 quadrillion possible strategies to consider for the four players. That didn't seem tractable, especially in the weekend we have to solve the problem. So, I first assumed they all used the same strategy. (I assumed this would fail, since they wouldn't know where they'd be in the circle.) I labeled the players 0, 1, 2, and 3 going counterclockwise so their left and right would be the same as the left and right of the list of players. I labeled the hat colors 0, 1, and 2 in order of increasing frequency (i.e., red, yellow, blue). The Python code is omitted for the sake of brevity, but it looks a lot like the code that finally works.

The result: no luck. The first equal-best strat I found was [(1, 0, 0), (1, 2, 1), (2, 2, 0)], where the row index is the color of the hat on your left and the column index was the color of the hat on the right -- e.g. if the left hat was yellow and the right hat was blue, guess strat[1][2] = 1 = yellow. The overall description for this strategy was at least easy enough to describe in words: 

Strategy A: If your neighbors have the same color hat, guess the "next" color. 
If they don't, guess the same color as the person to your left.
("next" = red -> yellow -> blue -> red, or (color + 1) % 3.)

A more verbose version of that code shows this strategy only fails when everyone's hat is the same color. Not bad, but apparently not good enough. I tried changing one person's strategy so that if they saw the same color hat on their neighbors, they'd guess that color. That didn't work, either. I tried every possible strategy for one person while the others used Strategy A: no help, either.

Next up: two strategies shared among the four players. This could be done in essentially three ways: player 0 has a unique strategy; players 0 and 1 share a strategy; and players 0 and 2 share a strategy. I got a slightly better result, with 79 successes:

Player 0: [(0, 0, 0), (1, 1, 2), (1, 0, 0)]
Players 1, 2, and 3: [(1, 0, 0), (1, 2, 2), (1, 0, 0)]

This fails when Player 0's hat is blue and everyone else's hats are either all yellow or all blue. Simple changes to the strategies of the failure states didn't help.

The code I wrote didn't have a progress indicator. So, after waiting a while, I killed the script and rewrote it with a progress indicator. Furthermore, I turned the for-hats-loop into a check_perfection() function that only returns 0 or 81. (It should've returned True or False, but I was lazy.) Then, I wrote more Python code around it.

Once I got to "Checking (0, 2, 1, 1, 2)..." (i.e., the first five steps of strategy 0), I realized that the symmetry of the problem meant that if there was a solution, there would be a symmetric version of it where the first digit of the raw strategy is 0 and the first non-zero digit is 1. So, there weren't any solutions with only two total strategies.

What about three? For this, I shifted to C++. Instead of making separate 3x3 arrays for each strategy, I used the raw_strat (i.e. every 27-digit number in ternary, renamed r for the C++ version) directly and calculated where in that array the result of each strategy based on the hats of the left and right players.The rest of the code was similar to the Python version, with itertools.product replace with a boatload of for loops:

iterate(0, 1, 2, 2) means that player 0 uses the strategy corresponding to r[0 thru 8], player 1 uses the strategy corresponding to r[9 thru 17], and players 2 and 3 use the strategy corresponding to r[18 thru 26]. This meant that the people sharing a strategy are neighbors; if this failed to give a result, I would try iterate(0, 2, 1, 2).

Fortunately, it worked! After a couple of hours, it spat out an answer amongst the progress updates:

0: 001012122; 1: 221210100; 23: 100210221 = 81

Putting it into words:
Player 0: Add the colors without modulo. 
* 0 or 1: red
* 2: yellow
* 3 or 4: blue

Player 1: Add the colors without modulo.
* 0 or 1: blue
* 2: yellow
* 3 or 4: red

Players 2 and 3: Subtract the colors (left - right) without modulo.
* -2 or -1: red
* 0: yellow
* 1 or 2: blue

I believe this is the equivalent of what I put in the answer blank.

I rewrote my test loop to use a more explicit version of my strategies, using Python 3.10's new match/case syntax:


The first four numbers are the actual placements of the hats. If they're wrapped in < and >, that hat was guessed correctly by its wearer. Following that is a list of the guesses made. If only one player guessed correctly, their number is listed, followed by the colors of the hats they saw in left-right order. So we've got an answer. Yay!
