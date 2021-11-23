import itertools

def sgn(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

def test_sgn():
    for a, b, c, d in itertools.product(range(-1, 2), repeat=4):
        ga = sgn(d + b)
        gb = sgn(-a - c)
        gc = sgn(b - d)
        gd = sgn(c - a)
        print(a, b, c, d, '|', ga, gb, gc, gd, '|', end=' ')

        out = 'Y' if a == ga else 'n'
        out += 'Y' if b == gb else 'n'
        out += 'Y' if c == gc else 'n'
        out += 'Y' if d == gd else 'n'
        print(out, end=' ')
        if out == 'nnnn': print('*** FAILURE ***')
        else: print()

test_sgn()
