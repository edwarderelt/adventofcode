import re
with open("03/input.txt", "r") as f:
    data = f.read()

pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
matches = re.findall(pattern, data)
print(matches)

total = 0
multiply = True
for match in matches:
    if match == "don't()":
        multiply = False
    elif match == "do()":
        multiply = True
    elif multiply:
        l, r = match.split(",")
        l = int(l[4:])
        r = int(r[:-1])
        print(l, r)
        total += l * r

print(total)
