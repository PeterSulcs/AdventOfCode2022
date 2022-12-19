BACK = (0.5, 0.5, 0)
BOTTOM = (0.5, 0, 0.5)
LEFT = (0, 0.5, 0.5)
RIGHT = (1.0,0.5,0.5)
TOP = (0.5,1.0,0.5)
FRONT = (0.5, 0.5, 1.0)

FILE = "input.txt"

def add_(origin, offset):
    return tuple(x+y for x,y in zip(origin, offset))


def get_midpoint_of_sides(origin):
    sides = list()
    for offset in [BACK, BOTTOM, LEFT, RIGHT, TOP, FRONT]:
        sides.append(add_(origin, offset))
    return sides

if __name__ == "__main__":
    midpoints = set()
    with open(FILE, "r") as fid:
        for line in fid:
            origin = tuple(int(x) for x in line.split(","))
            print(origin)
            results = get_midpoint_of_sides(origin)
            for r in results:
                if not (r in midpoints):
                    midpoints.add(r)
                else:
                    midpoints.remove(r)


    print(len(midpoints))

