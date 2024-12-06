rules = {}
changes = []
store_rules = True
with open("05/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            store_rules = False
        elif store_rules:
            l, r = line.split("|")
            l, r = int(l), int(r)
            rules[l] = rules.get(l, set())
            rules[l].add(r)
        else:
            int_line = [int(i) for i in line.strip().split(",")]
            changes.append(int_line)

print(rules)
print(changes)


total = 0
for change in changes:
    valid_change = True
    for i in range(len(change)):
        if not valid_change:
            break
        if change[i] in rules:
            for j in range(i):
                if change[j] in rules[change[i]]:
                    valid_change = False
                    break
    if valid_change:
        mid = change[len(change)//2]
        total += mid

print(total)
