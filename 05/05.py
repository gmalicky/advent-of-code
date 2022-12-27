"""
--- Day 5: Supply Stacks ---
After the rearrangement procedure completes, what crate ends up on top of each stack? (move one crate at once)
--- Part Two ---
After the rearrangement procedure completes, what crate ends up on top of each stack? (move multiple crates at once)
"""
from copy import deepcopy

with open('05/input.txt') as f:
    input = f.read()
start_position, instructions = input.split('\n\n')


def log_top_of_stacks(stacks):
    print("Top of each stack:")
    for stack in stacks:
        print(stack[-1], end='')


instructions = instructions.splitlines()
instructions = tuple(tuple(instruction.split()[1::2]) for instruction in instructions)
start_lines = start_position.splitlines()
del start_lines[-1]
start_lines = [line[1::4] for line in start_lines]

# setup of initial position of crates in stacks
stacks = [[] for _ in range(len(start_lines[0]))]
start_lines.reverse()
for line in start_lines:
    for i, box in enumerate(line):
        if box != ' ':
            stacks[i].append(box)
stacks2 = deepcopy(stacks)

# moving crates between stacks by one
for instruction in instructions:
    for _ in range(int(instruction[0])):
        box_to_move = stacks[int(instruction[1]) - 1].pop()
        stacks[int(instruction[2]) - 1].append(box_to_move)

log_top_of_stacks(stacks)

print("\n--- Part Two ---")

# moving crates between stacks at once
for instruction in instructions:
    start_move_index = -int(instruction[0])
    boxes_to_move = stacks2[int(instruction[1]) - 1][start_move_index:]
    del stacks2[int(instruction[1]) - 1][start_move_index:]
    stacks2[int(instruction[2]) - 1] += boxes_to_move

log_top_of_stacks(stacks2)
