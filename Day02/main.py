# Scoring

# The score for a single round is the score for the shape you selected 
# (1 for R, 2 for P, and 3 for S) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

import sys
FILE = sys.argv[1]

theirs_map = {
    "A": "R",
    "B": "P",
    "C": "S"
}
yours_map = {
    "X": "R",
    "Y": "P",
    "Z": "S"
}
value_map = {
    "R": 1,
    "P": 2,
    "S": 3
}


def get_score(strat):
    
    theirs_coded, yours_coded  = strat.strip().split(" ")
    yours = yours_map[yours_coded]
    theirs = theirs_map[theirs_coded]
    score = value_map[yours]
    win = is_win(yours,theirs)
    score += win
    # print(f"{yours} vs {theirs}, {value_map[yours]}, {win}, total_score: {score}" )
    return score

def is_win(a,b):
    if a == "S":
        if b == "P":
            return 6
        if b == "R":
            return 0
        else:
            return 3
    elif a == "P":
        if b == "S":
            return 0
        elif b == "R":
            return 6
        else:
            return 3
    else:
        if b == "S":
            return 6
        elif b == "P":
            return 0
        else:
            return 3

def to_follow(a, outcome):
    if a == "S":
        if outcome == "win":
            return "R"
        if outcome == "lose":
            return "P"
        else:
            return "S"
    elif a == "P":
        if outcome == "win":
            return "S"
        elif outcome == "lose":
            return "R"
        else:
            return "P"
    else:
        if outcome == "win":
            return "P"
        elif outcome == "lose":
            return "S"
        else:
            return "R"

action_map = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

# Part 1
score = 0
with open(FILE, 'r') as fid:
    for line in fid:
        score += get_score(line)

print(f" Part 1: {score}")


# Part 2

def get_score_part_2(strat):
    print(f"{strat.strip()}")
    theirs_coded, outcome_coded  = strat.strip().split(" ")
    theirs = theirs_map[theirs_coded]
    outcome = action_map[outcome_coded]
    print(f"You should: {outcome}")
    yours = to_follow(theirs, outcome)

    score = value_map[yours]
    win = is_win(yours,theirs)
    score += win
    print(f"{yours} vs {theirs}, {value_map[yours]}, {win}, total_score: {score}" )
    return score



score = 0
with open(FILE, "r") as fid:
    for line in fid:
        score += get_score_part_2(line)

print(f"Part 2: {score}")
