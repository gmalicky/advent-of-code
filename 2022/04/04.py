"""
--- Day 4: Camp Cleanup ---
In how many assignment pairs does one range fully contain the other?
--- Part Two ---
In how many assignment pairs do the ranges overlap?
"""

with open("input.txt") as f:
    input = f.read()
pairs = input.split()

count_contains = 0
count_overlaps = 0
for pair in pairs:
    first, second = pair.split(",")
    first_indexes = first.split("-")
    second_indexes = second.split("-")

    first_range = range(int(first_indexes[0]), int(first_indexes[1]) + 1)
    second_range = range(int(second_indexes[0]), int(second_indexes[1]) + 1)

    # if one contains the other
    if set(first_range).issubset(second_range) or set(first_range).issuperset(
        second_range
    ):
        count_contains += 1
    # if one overlaps with other
    if not set(first_range).isdisjoint(second_range):
        count_overlaps += 1

print(f"One range fully contains the other in {count_contains} pairs.")
print(f"One range overlaps with other in {count_overlaps} pairs.")
