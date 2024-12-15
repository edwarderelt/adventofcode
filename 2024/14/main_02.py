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
import copy
default_grid = copy.deepcopy(grid)

# for position in positions:
#     grid[position[1]][position[0]] = 1

STEPS = 100

import numpy as np

def entropy(grid):
    marg = np.histogramdd(np.ravel(grid), bins = 4)[0]/grid.size
    marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    return -np.sum(np.multiply(marg, np.log2(marg)))

def runs_entropy(grid):
    # Flatten the grid
    flat = np.ravel(grid)
    
    # Count number of value changes
    changes = sum(1 for i in range(1, len(flat)) if flat[i] != flat[i-1])
    
    # Normalize by length-1 (maximum possible changes)
    return changes / (len(flat) - 1)

lowest_entropy = float("inf")

for s in range(10000):
    grid = copy.deepcopy(default_grid)
    for velocity, position in zip(velocities, positions):
        new_position = ((position[0] + velocity[0] * s) % W, (position[1] + velocity[1] * s) % H)
        grid[new_position[1]][new_position[0]] += 1

    py_grid = np.array(grid, dtype=np.int32)
    current_entropy = runs_entropy(py_grid)
    if current_entropy < lowest_entropy:
        lowest_entropy = current_entropy
        print("##########################")
        print(f"Step {s}")
        print(f"New lowest entropy: {lowest_entropy}")
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    grid[i][j] = "."
        for row in grid:
            print("".join(str(cell) for cell in row))

