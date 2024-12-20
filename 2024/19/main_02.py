with open('19/input.txt', 'r') as f:
    data = f.readlines()

towels = data[0].strip().split(', ')
patterns = []
for line in data[2:]:
    patterns.append(line.strip())

print(towels)
print(patterns)

total_count = 0
patterns_that_can_be_made = {}
total_iters = 0
def check_can_make(pattern):
    global total_count
    global patterns_that_can_be_made
    global total_iters
    total_iters += 1
    can_make_count = 0
    if pattern in patterns_that_can_be_made:
        total_count += patterns_that_can_be_made[pattern]
        return patterns_that_can_be_made[pattern]
    for towel in towels:
        if pattern.startswith(towel):
            new_pattern = pattern[len(towel):]
            if new_pattern == '':
                total_count += 1
                print(total_count)
                can_make_count += 1
            else:
                can_make_count += check_can_make(new_pattern)
    patterns_that_can_be_made[pattern] = can_make_count
    return can_make_count

count = 0
i = 0
for pattern in patterns:
    if check_can_make(pattern):
        count += 1
    i += 1
    print(f"Pattern {i} of {len(patterns)}")
print(f"Total count: {total_count}")
# print(patterns_that_can_be_made)
# print(f"Total iters: {total_iters}")
# print(count)