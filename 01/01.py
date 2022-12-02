"""
--- Day 1: Calorie Counting ---
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
--- Part Two ---
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

with open('01/input.txt') as f:
    input = f.read()

# split input per elf
elves = input.split(sep='\n\n')

# calories of each elf
calories = []

for elf in elves:
    total_calories = 0

    elf_items = elf.split()
    for item in elf_items:
        total_calories += int(item)
    calories.append(total_calories)

calories.sort(reverse=True)

for i in range(3):
    print(f"{i + 1}. place: {calories[i]} calories")
print(f"Total of top 3 elves: {sum(calories[:3])}")
