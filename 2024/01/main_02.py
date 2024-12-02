with open("01/input.txt", "r") as f:
    data = f.read()

total = 0

firsts = []
seconds = {}
for line in data.splitlines():
    first, second = line.split("  ")
    firsts.append(int(first))
    seconds[int(second)] = seconds.get(int(second), 0) + 1

firsts.sort()

for i in range(len(firsts)):
    print(firsts[i], seconds.get(firsts[i],0))
    total += firsts[i]*seconds.get(firsts[i],0)

print(total)
