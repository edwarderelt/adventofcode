import sys
sys.setrecursionlimit(10000)

TEST = True
if TEST:
    H = 7
    W = 7
    bytes_to_fall = 12
    input_file = "18/input_test.txt"
else:
    H = 71
    W = 71
    bytes_to_fall = 1024
    input_file = "18/input.txt"
matrix = [["." for _ in range(W)] for _ in range(H)]
    
with open(input_file, "r") as f:
    lines = f.readlines()
for i in range(bytes_to_fall):
    Y, X = lines[i].strip().split(",")[0], lines[i].strip().split(",")[1]
    print(Y, X)
    matrix[int(X)][int(Y)] = "#"

for row in matrix:
    print("".join(row))

matrix[len(matrix)-1][len(matrix[0])-1] = "E"


start_i, start_j = 0, 0

print("start_i, start_j", start_i, start_j)
global_furthest_reached = 0
global_lowest_cost = float("inf")

lowest_costs = {}

def explore(explored: set, i: int, j: int, direction: str, previous_cost: int) -> int:
   
    global global_furthest_reached
    global global_lowest_cost
    global lowest_costs
    if (len(matrix)-1-i)*j > global_furthest_reached:
        global_furthest_reached = (len(matrix)-1-i)*j
        #print("Reached: i", (len(matrix)-1-i), "j", j)
    previous_cost += 1
    if (i, j, direction) in lowest_costs and previous_cost >= lowest_costs[(i, j, direction)]:
        return
    
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or (i, j) in explored or matrix[i][j] == "#":
        return float("inf")
    if matrix[i][j] == "E":
        global_lowest_cost = min(global_lowest_cost, previous_cost)
        print("Reached E with cost", global_lowest_cost)
        return
    
    lowest_costs[(i, j, direction)] = min(lowest_costs.get((i, j, direction), float("inf")), previous_cost)
    # up
    explored_copy = explored.copy()
    explore(explored_copy, i-1, j, "^", previous_cost)
    # down
    explored_copy = explored.copy()
    explore(explored_copy, i+1, j, "v", previous_cost)
    # left
    explored_copy = explored.copy()
    explore(explored_copy, i, j-1, "<", previous_cost)
    # right
    explored_copy = explored.copy()
    explore(explored_copy, i, j+1, ">", previous_cost)

    

explore(set(), start_i, start_j, ">", -1)
#176632
#171600
#168596
#90460