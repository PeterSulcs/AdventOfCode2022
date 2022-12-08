import sys
from collections import deque
import math

FILE = sys.argv[1]

number_of_piles = None
len_of_line = None
moves = list()
actions = list()
with open(FILE,'r') as fid:
    for line in fid:
        if len_of_line is None:
            len_of_line == len(line)
        if number_of_piles is None:
            number_of_piles = math.ceil(len(line.strip("\n"))/4)
            # print(f"number_of_piles: {number_of_piles}")
            piles = [deque() for x in range(0,number_of_piles)]
            # print(len(piles))

        m = 0
        n = 0
        if not line.startswith("move") and not line.startswith(" 1 "):
            for char in line:
                m += 1
                if m == 2:
                    the_char = char
                if m == 4:
                    # print(f"{n}, {the_char}")
                    m = 0
                    # print(f"n : {n}")
                    if the_char != " ":
                        # print("add char")
                        piles[n].append(the_char)
                    n += 1
        else:
            if line.startswith("move"):
                # print(line)
                first, second = line.split(" from ")
                move = int(first.replace("move ",""))
                _from, _to = second.split(" to ")
                actions.append([move,int(_from),int(_to)])
                # print(f"{move}, {_from} - {_to}")

state_of_piles = [pile for pile in piles]
print(state_of_piles)

for action in actions:
    move, _from, _to = action
    print(f"{move}, {_from}, {_to}")
    to_move = []
    for _ in range(0,move):
        a = piles[_from-1].popleft()
        print(f"moving {a} from {_from} to {_to}")
        to_move.append(a)

    to_move.reverse()
    for a in to_move:
        piles[_to-1].appendleft(a)
        state_of_piles = [pile for pile in piles]
    print(f"current: {state_of_piles}")       

state_of_piles = [pile for pile in piles]
print(state_of_piles)



print(actions)
[print(pile for pile in piles)]

print("".join([pile.popleft() for pile in piles]))