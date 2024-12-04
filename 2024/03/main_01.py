import re
with open("03/input.txt", "r") as f:
    data = f.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, data)
print(matches)

total = 0
for match in matches:
    l, r = match.split(",")
    l = int(l[4:])
    r = int(r[:-1])
    print(l, r)
    total += l * r

print(total)
