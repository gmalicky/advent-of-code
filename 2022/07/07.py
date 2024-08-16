"""
--- Day 7: No Space Left On Device ---
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
--- Part Two ---
Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""

with open("input.txt") as f:
    input = f.read()

tree = {"/": {}}
dir_sizes = {}


def create_file_tree(input):
    pwd = []
    for cmd in input:
        cmd_parts = cmd.split()
        if cmd.startswith("$"):
            # command
            if cmd_parts[1] == "cd":
                # change working directory
                folder = cmd_parts[-1]
                match (folder):
                    case "/":
                        pwd = ["/"]
                    case "..":
                        pwd.pop()
                    case _:
                        pwd.append(folder)
        elif cmd.startswith("dir"):
            # directory info
            folder_name = cmd_parts[-1]
            create_in_path(pwd, folder_name, {})
        else:
            # file info
            size, filename = cmd_parts
            create_in_path(pwd, filename, size)


def create_in_path(path, key, value):
    # navigate to correct path
    subtree = tree
    for dir in path:
        subtree = subtree.get(dir)
    subtree.setdefault(key, value)


def count_dir_sizes(subtree, path):
    for k, v in subtree.items():
        if isinstance(v, dict):
            # if folder, cd, add to results and recurse
            path.append(k)
            dir_sizes.setdefault("/".join(path), 0)
            count_dir_sizes(v, path)
        else:
            # if file, add its size to all folders in path
            for dir in ["/".join(path[: i + 1]) for i in range(len(path))]:
                dir_sizes[dir] += int(v)
        if k == path[-1]:
            # if end of folder reached, cd ..
            path.pop()


cmds = input.splitlines()
create_file_tree(cmds)
path = []
count_dir_sizes(tree, path)

total_size = 0
for size in dir_sizes.values():
    if size < 100000:
        total_size += size
print(f"Total size of directories with sizes less than 100000: {total_size}")

print("--- Part Two ---")

# needed - unused
to_delete = 30000000 - (70000000 - dir_sizes["/"])
candidate_to_delete_size = 30000000

for size in dir_sizes.values():
    if candidate_to_delete_size > size >= to_delete:
        candidate_to_delete_size = size
print(f"Size of the directory to delete: {candidate_to_delete_size}")
