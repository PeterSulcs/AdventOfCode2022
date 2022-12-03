import sys

ALPHABET = list("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
FILE = sys.argv[1]

def get_priority(c):
    """
    >>> get_priority("a")
    1
    >>> get_priority("A")
    27
    >>> get_priority("p")
    16
    >>> get_priority("P")
    42
    """
    return ALPHABET.index(c)

# Part 1
with open(FILE,'r') as fid:
    total_priorities = 0
    for line in fid:
        line = line.strip()
        first, second = line[0:int(len(line)/2)], line[int(len(line)/2):]
        print(f"{line} = {first} : {second}")
        in_common = set(first).intersection(set(second))
        print(f"{in_common}")
        for item in in_common:
            total_priorities += get_priority(item)

print(f"Final: {total_priorities}")
        
def generate_groups():
    group_size = 3
    n = 0
    group = []
    with open(FILE,'r') as fid:
        for line in fid:
            n += 1
            group.append(line.strip())
            if n == 3:
                yield group
                group = []
                n = 0


# Part 2
total_priorities = 0
for group in generate_groups():
    print(f"group {group}")
    a, b, c = [set(x) for x in group]
    badges = a.intersection(b.intersection(c))
    for badge in badges:
        print(f"badge: {badge}, priority: {get_priority(badge)}")
        total_priorities += get_priority(badge)

print(f"Total priorities: {total_priorities}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()