velocities = []
positions = []

with open("14/input.txt", "r") as f:
    for line in f:
        split = line.strip().split()
        velocity = (int(split[1].split(",")[0].split("=")[1]), int(split[1].split(",")[1]))
        position = (int(split[0].split(",")[0].split("=")[1]), int(split[0].split(",")[1]))
        velocities.append(velocity)
        positions.append(position)

print(velocities)
print(positions)

H = 103
W = 101

grid = [[0 for _ in range(W)] for _ in range(H)]

# for position in positions:
#     grid[position[1]][position[0]] = 1

STEPS = 100

for velocity, position in zip(velocities, positions):
    new_position = ((position[0] + velocity[0] * STEPS) % W, (position[1] + velocity[1] * STEPS) % H)
    print(new_position)
    grid[new_position[1]][new_position[0]] += 1

for row in grid:
    print("".join(str(cell) for cell in row))

mid_h = H // 2
mid_w = W // 2
print(mid_h, mid_w)


total = 1
quadrant1 = [row[:mid_w] for row in grid[:mid_h]]
quadrant2 = [row[mid_w+1:] for row in grid[:mid_h]]
quadrant3 = [row[:mid_w] for row in grid[mid_h+1:]]
quadrant4 = [row[mid_w+1:] for row in grid[mid_h+1:]]

for quadrant in [quadrant1, quadrant2, quadrant3, quadrant4]:
    for row in quadrant:
        print("".join(str(cell) for cell in row))
    print()
    print(sum(sum(row) for row in quadrant))
    total *= sum(sum(row) for row in quadrant)

print(total)
