import sys
from collections import queue


FILE = sys.argv[1]

number_of_piles = None
len_of_line = None
with open(FILE,'r') as fid:
    for line in fid:
        if len_of_line is None:
            len_of_line == len(line)
        if number_of_piles is None:
            number_of_piles = int(len(line.strip())/4)
            piles = queue(str)*number_of_piles
        print(f"{line}")
        m = 0
        n = 0
        for char in line:
            m += 1
            if m == 2:
                the_char = char
            if m == 4:
                piles[n].enqueue(the_char)
        if len(line) < len_of_line:
            break


