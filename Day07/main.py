import sys
from collections import defaultdict

FILE = sys.argv[1]
dirs = defaultdict(lambda: {"files": list(), "path": "", "size": 0, "dirs": list(), "visited": 0})

def get_dir_name(p):
    return "/".join(p).replace("//","/")

curdir = None
file_count = 0 
p = []
with open(FILE, "r") as fid:
    for line in fid:
        line = line.strip()
        if line[0].isnumeric():
            file_count += 1
        if line.startswith("$"):
            # print(f"command! {line}")
            _, command = line.split(" ", maxsplit=1)
            if " " in command:  # is a `cd` command
                command, target_dir = command.split(" ")
                if target_dir == "..":
                    
                    _ = p.pop()
                    curdir = p[-1]
                    print(f".., p: {p}, curdir: {curdir}")
                    refdir = get_dir_name(p)
                    dirs[refdir]["visited"] += 1
                else:
                    print(f"else, target_dir = {target_dir}")
                    curdir = target_dir
                    p.append(curdir)
                    refdir = get_dir_name(p)
                    dirs[refdir]["visited"] += 1
                    dirs[refdir]["path"] = get_dir_name(p)
                    # print(f"p: {p}, curdir: {curdir}")
            else:  # is an ls command
                print(f"ls {p}")
                continue
        elif line.startswith("dir "):  # directory
            directory = line.split(" ")[1]
            refdir = get_dir_name(p)
            dirs[refdir]["dirs"].append(directory)
        else:  # file
            sz, name = line.split(" ")
            refdir = get_dir_name(p)
            dirs[refdir]["files"].append(name)
            for n in range(1,len(p)+1):
                print(p[0:n])
                refdir = get_dir_name(p[0:n])
                print(f"Add: {sz} to directory: {refdir}...")
                dirs[refdir]["size"]+= int(sz)


print(dirs)

total = 0
final_file_count = 0
sizes = list()
for k,v in dirs.items():
    sizes.append(v["size"])
    for f in v["files"]:
        final_file_count +=1
    if v["size"] <= 100_000:
        print(f' {v["size"]}\t{v["path"]}')
        total += v["size"]
    else:
        print(f'-{v["size"]}\t{v["path"]}')

print(total)
needed = 30000000- (70000000 - dirs["/"]["size"])
print(f"{file_count} vs. {final_file_count}")

print([x for x in sorted(sizes) if x > needed][0])