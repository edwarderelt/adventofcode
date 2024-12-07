matrix = []
with open("06/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "^":
            print(i, j)
            i_0 = i
            j_0 = j

result_matrix = []
for _ in range(len(matrix)):
    result_matrix.append([0] * len(matrix[0]))
print(result_matrix)
result_matrix[i_0][j_0] = 1
def move(start_i, start_j, direction):
    if direction == "U":
        for i in range(start_i - 1, -1, -1):
            if matrix[i][start_j]=="#":
                return i+1, start_j, "R"
            result_matrix[i][start_j] = 1
    elif direction == "D":
        for i in range(start_i + 1, len(matrix)):
            if matrix[i][start_j]=="#":
                return i-1, start_j, "L"
            result_matrix[i][start_j] = 1
    elif direction == "L":
        for j in range(start_j - 1, -1, -1):
            if matrix[start_i][j]=="#":
                return start_i, j+1, "U"
            result_matrix[start_i][j] = 1
    elif direction == "R":
        for j in range(start_j + 1, len(matrix[0])):
            if matrix[start_i][j]=="#":
                return start_i, j-1, "D"
            result_matrix[start_i][j] = 1
    
    return None, None, None

keep_moving = True
direction = "U"
while keep_moving:
    i_0, j_0, direction = move(i_0, j_0, direction)
    if i_0 is None:
        keep_moving = False
    else:
        print(i_0, j_0, direction)

for row in result_matrix:
    print(" ".join(map(str, row)))

total_sum = 0
for row in result_matrix:
    total_sum += sum(row)
print(total_sum)