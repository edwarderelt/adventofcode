with open("01/input.txt", "r") as f:
    data = f.read()

total = 0

firsts = []
seconds = []
for line in data.splitlines():
    first, second = line.split("  ")
    firsts.append(int(first))
    seconds.append(int(second))

firsts.sort()
seconds.sort()

for i in range(len(firsts)):
    print(abs(firsts[i] - seconds[i]))
    total += abs(firsts[i] - seconds[i])

print(total)
