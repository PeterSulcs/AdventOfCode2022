import sys
from collections import defaultdict

FILE = sys.argv[1]
dirs = defaultdict(lambda: {"files": list(), "path": "", "size": 0, "dirs": list(), "visited": 0})


curdir = None
p = []
with open(FILE, "r") as fid:
    for line in fid:
        line = line.strip()
        if line.startswith("$"):
            # print(f"command! {line}")
            _, command = line.split(" ", maxsplit=1)
            if " " in command:  # is a `cd` command
                command, target_dir = command.split(" ")
                if target_dir == "..":
                    _ = p.pop()
                    curdir = p[-1]
                    # print(f"p: {p}, curdir: {curdir}")
                    dirs[curdir]["visited"] += 1
                else:
                    curdir = target_dir
                    p.append(curdir)
                    dirs[curdir]["visited"] += 1
                    dirs[curdir]["path"] = "/".join(p).replace("//","/")
                    # print(f"p: {p}, curdir: {curdir}")
            else:  # is an ls command
                print(f"ls {p}")
                continue
        elif line.startswith("dir "):  # directory
            directory = line.split(" ")[1]
            dirs[curdir]["dirs"].append(directory)
        else:  # file
            sz, name = line.split(" ")
            dirs[curdir]["files"].append(name)
            for d in p:
                print(f"Add: {sz} to directory: {d}...")
                dirs[d]["size"]+= int(sz)


print(dirs)

total = 0
for k,v in dirs.items():
    if v["size"] <= 100000:
        print(f'{v["size"]}\t{v["path"]}')
        total += v["size"]

print(total)