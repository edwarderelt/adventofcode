import sys
sys.setrecursionlimit(10000)

matrix = []
with open("16/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

for row in matrix:
    print("".join(row))

turn_costs = {
    "^": {"^":0, ">":1000, "v":2000, "<":1000},
    "v": {"^":2000, ">":1000, "v":0, "<":1000},
    "<": {"^":1000, ">":2000, "v":1000, "<":0},
    ">": {"^":1000, ">":0, "v":1000, "<":2000}
}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            start_i, start_j = i, j
            break

print("start_i, start_j", start_i, start_j)
global_furthest_reached = 0
global_lowest_cost = float("inf")

lowest_costs = {}
import random
best_seats = set()

def explore(explored: set, i: int, j: int, direction: str, previous_cost: int) -> int:
   
    global global_furthest_reached
    global global_lowest_cost
    global lowest_costs
    global best_seats
    if (len(matrix)-1-i)*j > global_furthest_reached:
        global_furthest_reached = (len(matrix)-1-i)*j
        print("Reached: i", (len(matrix)-1-i), "j", j)
    previous_cost += 1
    if previous_cost > 90460:
        return
    
    if (i, j, direction) in lowest_costs and previous_cost > lowest_costs[(i, j, direction)]:
        return

    explored.add((i, j))
    
    if matrix[i][j] == "#":
        return float("inf")
    if matrix[i][j] == "E":
        if previous_cost < global_lowest_cost:
            global_lowest_cost = previous_cost
            best_seats = explored.copy()
            print("Reached E with cost", global_lowest_cost)
        elif previous_cost == global_lowest_cost:
            best_seats |= explored.copy()
            print("Reached E with cost", global_lowest_cost)
        return
    
    lowest_costs[(i, j, direction)] = min(lowest_costs.get((i, j, direction), float("inf")), previous_cost)
    # up
    explored_copy = explored.copy()
    explore(explored_copy, i-1, j, "^", previous_cost + turn_costs[direction]["^"])
    # down
    explored_copy = explored.copy()
    explore(explored_copy, i+1, j, "v", previous_cost + turn_costs[direction]["v"])
    # left
    explored_copy = explored.copy()
    explore(explored_copy, i, j-1, "<", previous_cost + turn_costs[direction]["<"])
    # right
    explored_copy = explored.copy()
    explore(explored_copy, i, j+1, ">", previous_cost + turn_costs[direction][">"])

    

explore(set(), start_i, start_j, ">", -1)
print(len(best_seats))
#176632
#171600
#168596
#90460