"""
--- Day 2: Rock Paper Scissors ---
What would your total score be if everything goes exactly according to your strategy guide?
--- Part Two ---
Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

with open('02/input.txt') as f:
    input = f.read()
rounds = input.split(sep='\n')[:-1]


def map_to_symbol(letter):
    return [i for i in [rock, paper, scissors] if letter in i][0]


# symbols with scores
rock = ('A', 'X', 1)
paper = ('B', 'Y', 2)
scissors = ('C', 'Z', 3)

total_score = 0
for round in rounds:
    score = 0
    ai, me = round.split()
    ai = map_to_symbol(ai)
    me = map_to_symbol(me)

    # score for symbol
    score += me[2]
    # score for result
    if ai == me:
        score += 3
    elif (ai == rock and me == paper) or (ai == paper and me == scissors) or (ai == scissors and me == rock):
        score += 6

    total_score += score

print(f"Total score is: {total_score} points.")

print("--- Part Two ---")

total_score = 0
for round in rounds:
    score = 0
    ai, me = round.split()
    ai = map_to_symbol(ai)

    chosen = ()
    # score for result
    if me == 'Y':
        chosen = ai
        score += 3
    elif me == 'X':
        if ai == rock:
            chosen = scissors
        elif ai == paper:
            chosen = rock
        elif ai == scissors:
            chosen = paper
    elif me == 'Z':
        if ai == rock:
            chosen = paper
        elif ai == paper:
            chosen = scissors
        elif ai == scissors:
            chosen = rock
        score += 6
    # score for symbol
    score += chosen[2]

    total_score += score

print(f"Total score is: {total_score} points.")
