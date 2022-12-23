from icecream import ic
import math


def get_index(current, move, length):
    if move == 0:
        return current
    elif move < 0: # negative wrap around
        return (current + move - 1) % length
    elif move > 0: # positive wrap around
        return (current + move + 1) % length
    else:
        return (current + move) % length

def get_index_original(current, move, length):
    num_cross = math.floor(abs(move)/length)
    ic(num_cross)
    if move == 0:
        return current
    elif move < 0: # negative wrap around
        return (current + move - 1 - num_cross) % length
    elif move > 0: # positive wrap around
        return (current + move + 1 + num_cross) % length


# print("Initial arrangement:")
# print(", ".join([str(x) for x,_ in indexed_original]))

if __name__ == "__main__":

    FILE = "simple_input.txt"


    original = list()
    with open(FILE, 'r') as fid:
        for line in fid:
            original.append(int(line))

    ic(len(original))
    ic(max(original))
    ic(min(original))

    #ic.disable()
    # There ARE duplicates so we need to retain original coordinates to be 
    # able to locate the number to move
    indexed_original = [(x,y) for x, y in zip(original,range(0,len(original)))]
    indexed = [(x,y) for x, y in zip(original,range(0,len(original)))]


    LENGTH = len(original)
    for val,i in indexed_original:
        # print()
        current_index = indexed.index((val,i))
        # print(f"{val} moves between ")
        # move indexed[current_index] to_move spaces (including a wrap)
        a = indexed.pop(current_index)
        # to make things simple put a sentinel value back in
        indexed.insert(current_index, "X")
        new_index = get_index(current_index, val, LENGTH)
        indexed.insert(new_index, a)

        # remove sentinel
        b = indexed.index("X")
        _ = indexed.pop(b)
        
        ic([str(x) for x,_ in indexed])

    # find the zero
    final = [x for x,_ in indexed]

    start = final.index(0)
    a = (start+1000)%LENGTH
    b = (start+2000)%LENGTH
    c = (start+3000)%LENGTH


    print(f"{final[a]}")
    print(f"{final[b]}")
    print(f"{final[c]}")
    print(f"{final[a] + final[b] + final[c]}")
    # # print(indexed)
    # # print(f"{len(set(original))}, {len(original)}")


    # That's not the right answer. If you're stuck, make sure you're using 
    # the full input data; there are also some general tips on the about page,
    #  or you can ask for hints on the subreddit. 
    # Please wait one minute before trying again. (You guessed -13737.) [Return to Day 20]