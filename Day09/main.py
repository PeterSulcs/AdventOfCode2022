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


if __name__ == "__main__":
    s = (0,0)
    H = s
    T = s

    tail_positions = set()

    print(f"H {H}, T {T}")
    tail_positions.add(T)
    with open("input.txt", "r") as fid:
        for line in fid:
            direction, steps = line.strip().split(" ")
            steps = int(steps)
            for step in range(0, steps):
                H = move(H,direction)
                T = move_tail(T,H)
                tail_positions.add(T)
                print(f"Move {direction}, H {H}, T {T}")

    print(len(tail_positions))