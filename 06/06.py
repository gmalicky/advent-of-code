"""
--- Day 6: Tuning Trouble ---
How many characters need to be processed before the first start-of-packet marker is detected?
--- Part Two ---
How many characters need to be processed before the first start-of-message marker is detected?
"""

with open('06/input.txt') as f:
    input = f.read()


def find_start_of_marker(unique, name):
    buffer = []
    for i, char in enumerate(input):
        buffer.append(char)
        if len(buffer) > unique:
            buffer.pop(0)
        if len(buffer) == unique:
            # if all x are unique we found the start
            if len(set(buffer)) == unique:
                print(f"Found start-of-{name} marker at position {i + 1} and it is '{buffer}'")
                break


find_start_of_marker(4, 'packet')

print("--- Part Two ---")

find_start_of_marker(14, 'message')
