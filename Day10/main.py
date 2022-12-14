cycle = 1
X = 1
cycles = dict()
    
cycles[cycle] = int(X)
with open("input.txt", "r") as fid:
    for line in fid:
        match line.strip().split(" ")[0]:
            case "noop":
                print(f"noop cycle 1 \t{cycle} {X}")
                cycle += 1
                X = X
                print(f"noop end \t{cycle} {X}")
                cycles[cycle] = int(X)
            case "addx":
                print(f"addx cycle 1 \t{cycle} {X}")
                cycle +=1
                cycles[cycle] = int(X)
                print(f"addx cycle 2 \t{cycle} {X}")
                cycle +=1
                _, val = line.strip().split(" ")
                X += int(val)
                cycles[cycle] = int(X)
                print(f"addx end \t{cycle} {X}")


print(cycles)

# 20th, 60th, 100th, 140th, 180th, and 220th

total = 0
for n in [20,60,100,140,180,220]:
    print(f"{n} * {cycles[n]} ({n*cycles[n]})")
    total += n * cycles[n]

print(f"total: {total}")

rows = list()
c = 0
for n in range(1,7):
    row = list()
    for m in range(0,40):
        c += 1
        X = cycles[c]
        print(f"cycle {c}, {X}, {m}")
        if abs(X - m)<=1: 
            row.append("#")
        else:
            row.append(" ")
    rows.append(row)

for row in rows:
    print("".join(row))