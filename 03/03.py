"""
--- Day 3: Rucksack Reorganization ---
Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
--- Part Two ---
Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
"""

with open('03/input.txt') as f:
    input = f.read()
rucksacks = input.split()


def get_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


total = 0
for rucksack in rucksacks:
    size = len(rucksack)
    left_pocket = set(rucksack[:size // 2])
    right_pocket = set(rucksack[size // 2:])

    # common item for both pockets
    common = left_pocket.intersection(right_pocket).pop()
    total += get_priority(common)

print(f"Sum of priorities in pockets is: {total}")

print("--- Part Two ---")

groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

total = 0
for group in groups:
    # common item for whole group (badge)
    common = set(group[0]).intersection(set(group[1]), set(group[2])).pop()
    total += get_priority(common)

print(f"Sum of priorities in groups of 3 is: {total}")
