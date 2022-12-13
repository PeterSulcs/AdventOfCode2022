from numpy import sign

def move(H,direction):
    match direction:
        case "U":
            H = (H[0],H[1]+1)
        case "D":
            H = (H[0],H[1]-1)
        case "R":
            H = (H[0]+1,H[1])
        case "L":
            H = (H[0]-1,H[1])
        case _:
            print("recognized direction!!")
    return H

def move_tail(T,H):
    delta_x = H[0]-T[0]  # +, H is to right, - H is to left
    delta_y = H[1]-T[1]  # +, H is above,    - H is below
    abs_delta_x = abs(delta_x)
    abs_delta_y = abs(delta_y)
    bump_x = sign(delta_x)*1
    bump_y = sign(delta_y)
    print(f"match {(abs_delta_x, abs_delta_y)}")
    match (abs_delta_x, abs_delta_y):
        case (1,2):
            return (T[0]+bump_x,T[1]+bump_y)
        case (2,1):
            return (T[0]+bump_x,T[1]+bump_y)
        case (2,0):
            return (T[0]+bump_x,T[1])
        case (0,2):
            return (T[0],T[1]+bump_y)
        case (2,2):
            return (T[0]+bump_x,T[1]+bump_y)
        case _:
            return T

def move_rope(segments, direction):
    print(len(segments))
    new_segments = list()
    H = segments.pop()
    H = move(H, direction)
    new_segments.insert(0, H)
    while len(segments) > 0: 
        k = segments.pop()
        new_k = move_tail(k, H)
        new_segments.insert(0, new_k)
        H = new_k
    return new_segments



if __name__ == "__main__":
    segments = [(0,0)]*10
    tail_positions = set()
    tail_positions.add(segments[0])
    with open("input.txt", "r") as fid:
        for line in fid:
            direction, steps = line.strip().split(" ")
            steps = int(steps)
            for step in range(0, steps):
                segments = move_rope(segments,direction)
                tail_positions.add(segments[0])
                print(f"Move {direction}, rope: {segments}")

    print(len(tail_positions))