from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

directions = defaultdict(list)
for line in lines:
    direction, amount = line.split()
    directions[direction].append(int(amount))

total_forward = sum(directions["forward"])
total_depth = sum(directions["down"]) - sum(directions["up"])

print(f"{total_forward * total_depth}")

# Part 2
aim = 0
directions_p2 = defaultdict(list)
for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    if direction == "forward":
        directions_p2[direction].append(amount)
        directions_p2["depth"].append(amount*aim)
    else:
        aim = aim + amount if direction == "down" else aim - amount
        #print(f"after {direction} {amount}, aim is now {aim}")

total_forward = sum(directions_p2["forward"])
total_depth = sum(directions_p2["depth"])
print(f"{total_forward * total_depth}")

    
