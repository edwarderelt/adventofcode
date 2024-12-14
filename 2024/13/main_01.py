def solve(behavior: dict[str, int]):
    numerator = behavior["X"] * behavior["BY"] - behavior["Y"] * behavior["BX"]
    denominator = behavior["AX"] * behavior["BY"] - behavior["AY"] * behavior["BX"]

    a = numerator / denominator
    b = (behavior["X"] - a * behavior["AX"]) / behavior["BX"]

    return a, b


with open("13/input.txt", "r") as f:
    lines = f.readlines()


behaviors = []
behavior = {}
for line in lines:
    split = line.strip().split(" ")
    if len(split) < 2:
        continue
    if split[1] == "A:":
        behavior = {"AX": int(split[2][2:-1]), "AY": int(split[3][2:])}
    elif split[1] == "B:":
        behavior["BX"] = int(split[2][2:-1])
        behavior["BY"] = int(split[3][2:])
    elif split[0] == "Prize:":
        behavior["X"] = int(split[1][2:-1])
        behavior["Y"] = int(split[2][2:])
        behaviors.append(behavior)
    else:
        continue

print(behaviors)
total = 0
for behavior in behaviors:
    a, b = solve(behavior)
    if a.is_integer() and b.is_integer():
        total += a * 3 + b
print(total)
