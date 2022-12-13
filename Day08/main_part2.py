import sys
import numpy as np

FILE = sys.argv[1]

rows = list()
with open(FILE, 'r') as fid:
    for line in fid:
        row = [int(x) for x in line.strip()]
        rows.append(row)

field = np.array(rows)
print(field)

# brute force:
n, m=field.shape

def trees_until_blocked(sequence):
    """
    includes first value
    >>> trees_until_blocked(np.array([4,3,1,7]))
    3
    >>> trees_until_blocked(np.array([5,3]))
    1
    """
    if len(sequence) == 0:
        return 0
    tree_height, rest = sequence[0], sequence[1:]
    if len(rest) > 0:
        rest_maxed = np.maximum.accumulate(rest)
        tree_count = np.min([np.array(tree_height>rest_maxed, dtype="int").sum()+1,len(rest)])
    else:
        tree_count = 0
    return tree_count

the_max = -1
for x in range(0,n):
    for y in range(0,m):
        lefts = field[x,0:(y+1)][::-1]
        left = trees_until_blocked(lefts)
        ups = field[0:(x+1),y][::-1]
        up = trees_until_blocked(ups)
        rights = field[x,y:]
        right = trees_until_blocked(rights)
        downs = field[x:,y]
        down = trees_until_blocked(downs)
        score = up*left*down*right
        if score > the_max:
            print(f"{x},{y}, ups: {ups}, lefts: {lefts}, downs: {downs}, rights{rights}, scenic: {up*left*down*right}")
            print(f"{x},{y}, up: {up}, left: {left}, down: {down}, right: {right}, scenic: {up*left*down*right}")
            the_max = score

if __name__ == "__main__":
    import doctest
    doctest.testmod()