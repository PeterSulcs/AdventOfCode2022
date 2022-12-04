import sys

FILE = sys.argv[1]

def encloses(a, b):
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    if a[0] <= b[0] and a[1] >= b[1]:
        return True
    return False

def overlap(a,b):
    if a[0] <= b[0]:
        first = a
        second = b
    else:
        first = b
        second = a
    if first[1] < second[0]:
        return False
    return True


with open(FILE, 'r') as fid:
    n = 0
    m = 0 
    for line in fid:
        a, b = [ [ int(y) for y in x.split("-")] for x in line.strip().split(",")]
        print(f"a: {a}, b: {b}, encloses: {encloses(a,b)}, overlaps: {overlap(a,b)}")
        if encloses(a,b):
            n += 1
        if overlap(a,b):
            m += 1

print(f"Total that enclose: {n}, total that overlap: {m}")


