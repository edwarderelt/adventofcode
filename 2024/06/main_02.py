matrix = []
with open("06/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

#print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "^":
            #print(i, j)
            i_0 = i
            j_0 = j


def check_loop(i_0, j_0, new_matrix):
    def move(start_i, start_j, direction):
        if direction == "U":
            for i in range(start_i - 1, -1, -1):
                if new_matrix[i][start_j]=="#":
                    return i+1, start_j, "R"
        elif direction == "D":
            for i in range(start_i + 1, len(matrix)):
                if new_matrix[i][start_j]=="#":
                    return i-1, start_j, "L"
        elif direction == "L":
            for j in range(start_j - 1, -1, -1):
                if new_matrix[start_i][j]=="#":
                    return start_i, j+1, "U"
        elif direction == "R":
            for j in range(start_j + 1, len(matrix[0])):
                if new_matrix[start_i][j]=="#":
                    return start_i, j-1, "D"
        
        return None, None, None

    keep_moving = True
    direction = "U"
    visited = set()
    while keep_moving:
        i_0, j_0, direction = move(i_0, j_0, direction)
        if (i_0, j_0, direction) in visited:
            return True
        if i_0 is None:
            return False
        else:
            visited.add((i_0, j_0, direction))


loop_count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "^":
            continue
        # copy matrix
        new_matrix = [row[:] for row in matrix]
        new_matrix[i][j] = "#"
        #print(new_matrix)
        if check_loop(i_0, j_0, new_matrix) is True:
            loop_count += 1

print("Loops: ", loop_count)

