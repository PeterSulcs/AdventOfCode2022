import sys

FILE = sys.argv[1]

elves = []
with open(FILE, 'r') as fid:
    elf = 0
    elves.append(0)
    for line in fid:
        if line.strip() == "":
            elf += 1
            elves.append(0)
        else:
            elves[elf] += int(line)

print(elves)

print(max(elves))

sorted_elves = sorted(elves, reverse=True)
print(f"Total of top three elves: {sum(sorted_elves[0:3])}")