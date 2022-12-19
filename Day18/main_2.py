from typing import Set

class face():

    def __init__(self, midpoint, normal):
        self.midpoint = midpoint
        self.normal = normal
    
    def __hash__(self):
        return hash(self.midpoint)

    def __eq__(self, other):
        return self.midpoint == other.midpoint

    def __repr__(self):
        return f"face({self.midpoint},{self.normal})"

    def __add__(self, other):
        return face(tuple(x+y for x,y in zip(self.midpoint, other.midpoint)), other.normal)

    def extend(self):
        return face(tuple(x+y for x,y in zip(self.midpoint, self.normal)), self.normal)


class bounds():
    def __init__(self, x_bounds, y_bounds, z_bounds):
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.z_bounds = z_bounds
    
    @classmethod
    def from_midpoints(cls, midpoints: Set[face]):
        xs = list()
        ys = list()
        zs = list()
        for f in midpoints:
            x,y,z = f.midpoint
            xs.append(x); ys.append(y); zs.append(z)
        print(f"xs: {xs} \n ys: {ys} \n zs: {zs}")
        return cls((min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs)))

    def within(self, point: face) -> bool:
        if self.x_bounds[0] <= point.midpoint[0] <= self.x_bounds[1]:
            if self.y_bounds[0] <= point.midpoint[1] <= self.y_bounds[1]:
                if self.z_bounds[0] <= point.midpoint[2] <= self.z_bounds[1]:
                    return True
        return False

    def __repr__(self):
        return f"bounds({self.x_bounds},{self.y_bounds},{self.z_bounds})"
        



BACK = face((0.5, 0.5, 0),(0,0,-1))
BOTTOM = face((0.5, 0, 0.5),(0,-1,0))
LEFT = face((0, 0.5, 0.5),(-1,0,0))
RIGHT = face((1.0,0.5,0.5),(1,0,0))
TOP = face((0.5,1.0,0.5),(0,1,0))
FRONT = face((0.5, 0.5, 1.0),(0,0,1))

FILE = "input.txt"

def add_(origin: face, offset: face):
    return face(tuple(x+y for x,y in zip(origin.midpoint, offset.midpoint)), offset.normal)


def get_midpoint_of_sides(origin: face):
    sides = list()
    for offset in [BACK, BOTTOM, LEFT, RIGHT, TOP, FRONT]:
        sides.append(origin + offset)
    return sides

def is_external(side: face, collection: Set[face], the_bounds: bounds) -> bool:
    test_point = side.extend()
    # print(f"is_external: test_point: {test_point}")
    while the_bounds.within(test_point):
        test_point = test_point.extend()
        # print(f"is_external extending...: test_point: {test_point}")
        if test_point in collection:
            print(f" is_external: side: {side}")
            print(f"  hit @ {test_point} this side")
            for c in collection:
                if c.midpoint == test_point.midpoint:
                    if c.normal == tuple(x for x in test_point.normal):
                        print(f"  the face: {c}")
                        return False
                    else:
                        return True  # desperation
    # print(f" hit bounds...")
    return True


if __name__ == "__main__":
    midpoints = set()
    with open(FILE, "r") as fid:
        for line in fid:
            origin = face(tuple(int(x) for x in line.split(",")),normal=(0,0,0))
            results = get_midpoint_of_sides(origin)
            for r in results:
                if not (r in midpoints):
                    midpoints.add(r)
                else:
                    midpoints.remove(r)

    print(len(midpoints))

    the_bounds = bounds.from_midpoints(midpoints)
    print(the_bounds)
    original_midpoints = midpoints.copy()
    for p in original_midpoints:
        print(f"{len(midpoints)}, {len(original_midpoints)}")
        if not is_external(p, original_midpoints, the_bounds):
            midpoints.remove(p)

    print(len(midpoints))

