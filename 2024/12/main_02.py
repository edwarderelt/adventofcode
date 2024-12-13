matrix = []
with open("12/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

print(matrix)
global_visited_patches = set()
def get_plot(i, j, visited_patches: set, edges: dict):
    if (i, j) in visited_patches:
        return 0
    visited_patches.add((i, j))
    global_visited_patches.add((i, j))
    area = 1
    if i > 0 and matrix[i-1][j] == matrix[i][j]:
        sub_area = get_plot(i-1, j, visited_patches, edges)
        area += sub_area
    else:
        edges[(i, j, "up")] = (i, j+1, "up")
    if i < len(matrix)-1 and matrix[i+1][j] == matrix[i][j]:
        sub_area = get_plot(i+1, j, visited_patches, edges)
        area += sub_area
    else:
        edges[(i, j, "down")] = (i, j+1, "down")
    if j > 0 and matrix[i][j-1] == matrix[i][j]:
        sub_area = get_plot(i, j-1, visited_patches, edges)
        area += sub_area
    else:
        edges[(i, j, "left")] = (i+1, j, "left")
    if j < len(matrix[i])-1 and matrix[i][j+1] == matrix[i][j]:
        sub_area = get_plot(i, j+1, visited_patches, edges)
        area += sub_area
    else:
        edges[(i, j, "right")] = (i+1, j, "right")

    return area

visited_patches = set()
# edges = {}
# print(get_plot(0, 0, visited_patches, edges))
# print(edges)
# print(len(edges.keys()))
import copy

def reduce_edges(edges: dict):
    keys = copy.deepcopy(edges).keys()
    for key in keys:
        edge = edges.get(key)
        while edge in edges:
            edges[key] = edges[edge]
            del edges[edge]
            edge = edges[key]

# reduce_edges(edges)

# print(edges)
# print(len(edges.keys()))

print("##########################")
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i, j) not in global_visited_patches:
            edges = {}
            area = get_plot(i, j, visited_patches, edges)
            reduce_edges(edges)
            perimeter = len(edges.keys())
            total += perimeter*area
            print(perimeter, area)

print(total)
