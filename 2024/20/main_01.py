import sys
sys.setrecursionlimit(10000)

matrix = []
with open("20/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

for row in matrix:
    print("".join(row))


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            start_i, start_j = i, j
            break

print("start_i, start_j", start_i, start_j)

hash_count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "#":
            hash_count += 1
print(hash_count)



global_lowest_cost = float("inf")
distances_from_start = {}

def explore(matrix_input: list[list[str]], explored: set, i: int, j: int, previous_cost: int, store_distances: bool = False) -> int:
    global global_lowest_cost
    global distances_from_start
    explored.add((i, j))
    previous_cost += 1
    
    if matrix_input[i][j] == "#":
        return float("inf")
    if store_distances:
        distances_from_start[(i, j)] = previous_cost
    if matrix_input[i][j] == "E":
        global_lowest_cost = min(global_lowest_cost, previous_cost)
        #print("Reached E with cost", global_lowest_cost)
        return
    # up
    explored_copy = explored.copy()
    if (i-1, j) not in explored:
        explore(matrix_input, explored_copy, i-1, j, previous_cost, store_distances)
    # down
    explored_copy = explored.copy()
    if (i+1, j) not in explored:
        explore(matrix_input, explored_copy, i+1, j, previous_cost, store_distances)
    # left
    explored_copy = explored.copy()
    if (i, j-1) not in explored:
        explore(matrix_input, explored_copy, i, j-1, previous_cost, store_distances)
    # right
    explored_copy = explored.copy()
    if (i, j+1) not in explored:
        explore(matrix_input, explored_copy, i, j+1, previous_cost, store_distances)

matrix_copy = [row[:] for row in matrix]
explore(matrix_copy, set(), start_i, start_j, -1, True)
original_cost = global_lowest_cost

print(distances_from_start)

cheat_positions = {}
cheat_positions2 = {}
for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[i])-1):
        if matrix[i][j] == "#":
            #print("###########################")
            local_cheat_positions = []
            if (i+1, j) in distances_from_start:
                local_cheat_positions.append(distances_from_start[(i+1, j)])
                #print(f"Down: {distances_from_start[(i+1, j)]}, {i+1}, {j}")
            if (i-1, j) in distances_from_start:
                local_cheat_positions.append(distances_from_start[(i-1, j)])
                #print(f"Up: {distances_from_start[(i-1, j)]}, {i-1}, {j}")
            if (i, j+1) in distances_from_start:
                local_cheat_positions.append(distances_from_start[(i, j+1)])
                #print(f"Right: {distances_from_start[(i, j+1)]}, {i}, {j+1}")
            if (i, j-1) in distances_from_start:
                local_cheat_positions.append(distances_from_start[(i, j-1)])
                #print(distances_from_start)
                #print(f"Left: {distances_from_start[(i, j-1)]}, {i}, {j-1}")
            if len(local_cheat_positions) >= 2:
                cheat_positions[(i, j)] = max(local_cheat_positions)-min(local_cheat_positions)-2
                #print(f"Optimal method: Cheat position: {i}, {j} with cost {cheat_positions[(i, j)]}")
            # matrix_copy = [row[:] for row in matrix]
            # matrix_copy[i][j] = "."
            # global_lowest_cost = float("inf")
            # explore(matrix_copy, set(), start_i, start_j, -1)
            # cheat_positions2[(i, j)] = original_cost - global_lowest_cost
            # print(f"Robust method: Cheat position: {i}, {j} with cost {cheat_positions2[(i, j)]}")

print(sorted(cheat_positions.values()))
# print(sorted(cheat_positions2.values()))
print(original_cost)

count = 0
for value in cheat_positions.values():
    if value >= 100:
        count += 1
print(count)