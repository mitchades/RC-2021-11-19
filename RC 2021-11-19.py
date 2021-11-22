import itertools

#########
# This was lifted from Stack Overflow.

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Assuming "mathy" ccw order for the players:
#
#    1
#  2 @ 0
#    3

#########
# This was the first function I wrote. It gave everyone the same
# strategy. Its best result was shown above.
            
def test_all_same():
    most_successes = 0
    for raw_strat in itertools.product(range(3), repeat=9):
        strat = list(chunks(raw_strat, 3))

        successes = 0
        for hats in itertools.product(range(3), repeat=4):
            guesses = [strat[hats[3]][hats[1]],
                       strat[hats[0]][hats[2]],
                       strat[hats[1]][hats[3]],
                       strat[hats[2]][hats[0]]]
            if (hats[0] == guesses[0] or
                hats[1] == guesses[1] or
                hats[2] == guesses[2] or
                hats[3] == guesses[3]):
                    successes += 1

        if successes > most_successes:
            most_successes = successes
            print(strat, successes)

# Results:
# bs = best single strategy
#    = person to your left, if left != right
#      1 + person to left (mod 3), if left == right
bs = [[1,0,0], [1,2,1], [2,2,0]]

#########
# The best single strategy I found only failed if all the hats were the
# same color. I tried giving 3 players that strategy and testing every
# possible strategy for the 0th player. It found no successful strategies.

def test_3_best():
    """s0 iterates; s1~3 are all [[1,0,0],[1,2,1],[2,2,0]]"""
    most_successes = 0
    for raw_strat in itertools.product(range(3), repeat=9):
        strat = list(chunks(raw_strat, 3))

        successes = 0
        for hats in itertools.product(range(3), repeat=4):
            guesses = [strat[hats[3]][hats[1]],
                       bs[hats[0]][hats[2]],
                       bs[hats[1]][hats[3]],
                       bs[hats[2]][hats[0]]]
            if (hats[0] == guesses[0] or
                hats[1] == guesses[1] or
                hats[2] == guesses[2] or
                hats[3] == guesses[3]):
                    successes += 1
        if successes > most_successes:
            most_successes = successes
            print(strat, successes)
            
# Things were about to get a lot slower. I realized I'd need a hat test that
# just returned pass or fail, which would allow it to return fail as soon
# as possible. I made a more verbose version as well, which could
# help me logic through an answer. (Spoiler: it didn't.)

#########
# This function checks all 3**4 == 81 arrangements of hats, returning
# the number of successes. In verbose mode, it prints all the results
# and indicates which arrangements were only guessed correctly by
# one player.

def check_all_hats(s0, s1, s2, s3, verbose=False):
    """s0~3 = 3x3 strategy for that player"""
    successes = 0
    for hats in itertools.product(range(3), repeat=4):
        guesses = [s0[hats[3]][hats[1]],
                   s1[hats[0]][hats[2]],
                   s2[hats[1]][hats[3]],
                   s3[hats[2]][hats[0]]]
        if (hats[0] == guesses[0] or hats[1] == guesses[1] or
            hats[2] == guesses[2] or hats[3] == guesses[3]):
                successes += 1
                if verbose:
                    correct_bits = 0
                    for h in range(4):
                        if hats[h] == guesses[h]:
                            print(f'<{hats[h]}>', end='')
                            correct_bits += 2**h
                        else:
                            print(f' {hats[h]} ', end='')
                    print(guesses, end='')
                    match correct_bits:
                        case 1:
                            print('Only player 0', hats[3], hats[1])
                        case 2:
                            print('Only player 1', hats[0], hats[2])
                        case 4:
                            print('Only player 2', hats[1], hats[3])
                        case 8:
                            print('Only player 3', hats[2], hats[0])
                        case _:
                            print('Success')
        elif verbose:
            print('***', hats, guesses, "Failure")
    if verbose: print("Total successes:", successes)
    return successes

#########
# This version of check_all_hats() wil return 0 as soon as it finds a
# failure. It returns 81 if everything works.

def check_perfection(s0, s1, s2, s3, verbose=False):
    """s0~3 = 3x3 strategy for that player"""
    for hats in itertools.product(range(3), repeat=4):
        guesses = [s0[hats[3]][hats[1]],
                   s1[hats[0]][hats[2]],
                   s2[hats[1]][hats[3]],
                   s3[hats[2]][hats[0]]]
        if (hats[0] != guesses[0] and hats[1] != guesses[1] and
            hats[2] != guesses[2] and hats[3] != guesses[3]):
                return 0
    return 81

#########
# This function checks every way to distribute two strategies
# between the players. It found no successful strategies.

def iterate2():
    fifth = -1
    for raw_strat in itertools.product(range(3), repeat=18):
        if fifth != raw_strat[4]:
            print(f"Checking {raw_strat[0:5]}...")
            fifth = raw_strat[4]
        s0 = list(chunks(raw_strat[0:9], 3))
        s1 = list(chunks(raw_strat[9:18], 3))
        successes = check_perfection(s0, s1, s1, s1)
        if successes == 81:
            print('0', s0, '1, 2, 3', s1, successes)
        successes = check_perfection(s0, s0, s1, s1)
        if successes == 81:
            print('0, 1', s0, '2, 3', s1, successes)
        successes = check_perfection(s0, s1, s0, s1)
        if successes == 81:
            print('0, 2', s0, '1, 3', s1, successes)
            
# The best result of the above using the check_all_hats() version:
# 0 [(0, 0, 0), (1, 1, 2), (1, 0, 0)]
# 1, 2, 3 [(1, 0, 0), (1, 2, 2), (1, 0, 0)] 79

#########
# After running this long enough to see it wouldn't work,
# I switched to C++ for iterate3(). 

# This is the answer I got from my C++ code:

# check_all_hats([[0,0,1],[0,1,2],[1,2,2]],
#                [[2,2,1],[2,1,0],[1,0,0]],
#                [[1,0,0],[2,1,0],[2,2,1]],
#                [[1,0,0],[2,1,0],[2,2,1]], verbose=True)

#########
# I wrote this version of the test function as a final check
# of my answer. Instead of a 4x3x3 nested list of guesses, 
# I used the inputs each player would see and match/case'd
# their guess from that.

def test_english(verbose=False):
    """Strategies based on what each player sees."""
    successes = 0
    for hats in itertools.product(range(3), repeat=4):
        guesses = [-1, -1, -1, -1]
        # Simulating player 0
        match hats[3] + hats[1]:
            case 0 | 1:
                guesses[0] = 0
            case 2:
                guesses[0] = 1
            case 3 | 4:
                guesses[0] = 2
        # Simulating player 1
        match hats[0] + hats[2]:
            case 0 | 1:
                guesses[1] = 2
            case 2:
                guesses[1] = 1
            case 3 | 4:
                guesses[1] = 0
        # Simulating player 2
        match hats[1] - hats[3]:
            case -2 | -1:
                guesses[2] = 0
            case 0:
                guesses[2] = 1
            case 1 | 2:
                guesses[2] = 2
        # Simulating player 3
        match hats[2] - hats[0]:
            case -2 | -1:
                guesses[3] = 0
            case 0:
                guesses[3] = 1
            case 1 | 2:
                guesses[3] = 2
        if (hats[0] == guesses[0] or hats[1] == guesses[1] or
            hats[2] == guesses[2] or hats[3] == guesses[3]):
                successes += 1
                if verbose:
                    correct_bits = 0
                    for h in range(4):
                        if hats[h] == guesses[h]:
                            print(f'<{hats[h]}>', end='')
                            correct_bits += 2**h
                        else:
                            print(f' {hats[h]} ', end='')
                    print(guesses, end='')
                    match correct_bits:
                        case 1:
                            print('Only player 0', hats[3], hats[1])
                        case 2:
                            print('Only player 1', hats[0], hats[2])
                        case 4:
                            print('Only player 2', hats[1], hats[3])
                        case 8:
                            print('Only player 3', hats[2], hats[0])
                        case _:
                            print('Success')
        elif verbose:
            print('***', hats, guesses, "Failure")
    if verbose: print("Total successes:", successes)
    return successes
