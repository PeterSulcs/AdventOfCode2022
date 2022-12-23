from icecream import ic

# Swap function
def swap_positions(the_list, pos1, pos2):
     
    # popping both the elements from the_list
    first_ele = the_list.pop(pos1)  
    second_ele = the_list.pop(pos2-1)
    
    # inserting in each others positions
    the_list.insert(pos1, second_ele) 
    the_list.insert(pos2, first_ele) 
    return the_list

# Hop Positions
def hop_right(the_list, pos):
    a = the_list.pop(pos)
    the_list.insert(pos+1, a)
    return pos+1

def hop_left(the_list, pos):
    a = the_list.pop(pos)
    the_list.insert(pos-1, a)
    return pos-1

def hop_wrap_right(the_list, pos):
    a = the_list.pop(pos)
    the_list.insert(1, a)
    return 1

def hop_wrap_left(the_list, pos):
    a = the_list.pop(pos)
    the_list.insert(-1, a)
    return len(the_list)-2

if __name__ == "__main__":

    FILE = "input.txt"


    original = list()
    with open(FILE, 'r') as fid:
        for line in fid:
            original.append(int(line))

    ic(len(original))
    ic(max(original))
    ic(min(original))

    ic.disable()
    # There ARE duplicates so we need to retain original coordinates to be 
    # able to locate the number to move
    indexed_original = [(x,y) for x, y in zip(original,range(0,len(original)))]
    indexed = [(x,y) for x, y in zip(original,range(0,len(original)))]


    LENGTH = len(original)
    for val,i in indexed_original:
        # print()
        current_index = indexed.index((val,i))

        moves = val
        while moves > 0:  # positive movement
            if current_index < (LENGTH-1):
                current_index = hop_right(indexed, current_index)
            else:
                current_index = hop_wrap_right(indexed, current_index)
            moves -= 1
            ic("right", indexed)

        while moves < 0:  # negative movement
            if current_index > 0:
                current_index = hop_left(indexed, current_index)
            else:
                current_index = hop_wrap_left(indexed, current_index)
            ic("left", indexed)
            moves += 1

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