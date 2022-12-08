import sys

FILE = sys.argv[1]
NUMBER_OF_CHARACTERS = 4

with open(FILE, 'r') as fid:
    for line in fid:
        buffer = list()
        n = 0
        for char in line:
            n += 1
            buffer.append(char)
            if len(buffer) > NUMBER_OF_CHARACTERS:
                _ = buffer.pop(0)
            if len(buffer) == NUMBER_OF_CHARACTERS:
                if len(set(buffer)) == len(buffer):
                    print(f"{buffer} is the marker after {n} characters processed!")
                    break

NUMBER_OF_CHARACTERS = 14
with open(FILE, 'r') as fid:
    for line in fid:
        buffer = list()
        n = 0
        for char in line:
            n += 1
            buffer.append(char)
            if len(buffer) > NUMBER_OF_CHARACTERS:
                _ = buffer.pop(0)
            if len(buffer) == NUMBER_OF_CHARACTERS:
                if len(set(buffer)) == len(buffer):
                    print(f"{buffer} is the start of message after {n} characters processed!")
                    break