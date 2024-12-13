matrix = []
with open("12/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

print(matrix)
global_visited_patches = set()
def get_plot(i, j, visited_patches):
    if (i, j) in visited_patches:
        return 0, 0
    visited_patches.add((i, j))
    global_visited_patches.add((i, j))
    perimeter = 0
    area = 1
    if i > 0 and matrix[i-1][j] == matrix[i][j]:
        sub_perimeter, sub_area = get_plot(i-1, j, visited_patches)
        perimeter += sub_perimeter
        area += sub_area
    else:
        perimeter += 1
    if i < len(matrix)-1 and matrix[i+1][j] == matrix[i][j]:
        sub_perimeter, sub_area = get_plot(i+1, j, visited_patches)
        perimeter += sub_perimeter
        area += sub_area
    else:
        perimeter += 1
    if j > 0 and matrix[i][j-1] == matrix[i][j]:
        sub_perimeter, sub_area = get_plot(i, j-1, visited_patches)
        perimeter += sub_perimeter
        area += sub_area
    else:
        perimeter += 1
    if j < len(matrix[i])-1 and matrix[i][j+1] == matrix[i][j]:
        sub_perimeter, sub_area = get_plot(i, j+1, visited_patches)
        perimeter += sub_perimeter
        area += sub_area
    else:
        perimeter += 1

    return perimeter, area

visited_patches = set()
#print(get_plot(0, 4, visited_patches))

print("##########################")
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i, j) not in global_visited_patches:
            perimeter, area = get_plot(i, j, visited_patches)
            total += perimeter*area
            print(perimeter, area)
print(total)
