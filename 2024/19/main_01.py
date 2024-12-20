with open('19/input.txt', 'r') as f:
    data = f.readlines()

towels = data[0].strip().split(', ')
patterns = []
for line in data[2:]:
    patterns.append(line.strip())

print(towels)
print(patterns)

def check_can_make(pattern):
    can_make = False
    for towel in towels:
        if pattern.startswith(towel):
            new_pattern = pattern[len(towel):]
            if new_pattern == '':
                can_make = True
            else:
                can_make = check_can_make(new_pattern)
            if can_make:
                return True
    return can_make

count = 0
i = 0
for pattern in patterns:
    if check_can_make(pattern):
        count += 1
    i += 1
    print(i)
print(count)
# print(check_can_make('bwurrg'))
