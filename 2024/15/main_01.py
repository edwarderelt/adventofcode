matrix = []
store_matrix = True
commands = ""
with open("15/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            store_matrix = False
            continue
        if store_matrix:
            matrix.append(list(line.strip()))
        else:
            commands += line.strip()

for row in matrix:
    print("".join(row))

print(commands)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "@":
            print(i, j)
            i_0 = i
            j_0 = j

def move(command, pos_i, pos_j):
    if command == "v":
        i = pos_i+1
        move_n = 1
        while matrix[i][pos_j] != "#":
            if matrix[i][pos_j] == ".":
                for move_i in range(pos_i+move_n, pos_i, -1):
                    matrix[move_i][pos_j] = matrix[move_i-1][pos_j]
                matrix[pos_i][pos_j] = "."
                return (pos_i+1, pos_j)
            i += 1
            move_n += 1
        return (pos_i, pos_j)
    elif command == "^":
        i = pos_i-1
        move_n = 1
        while matrix[i][pos_j] != "#":
            if matrix[i][pos_j] == ".":
                for move_i in range(pos_i-move_n, pos_i, 1):
                    matrix[move_i][pos_j] = matrix[move_i+1][pos_j]
                matrix[pos_i][pos_j] = "."
                return (pos_i-1, pos_j)
            i -= 1
            move_n += 1
        return (pos_i, pos_j)
    elif command == ">":
        j = pos_j+1
        move_n = 1
        while matrix[pos_i][j] != "#":
            if matrix[pos_i][j] == ".":
                for move_j in range(pos_j+move_n, pos_j, -1):
                    matrix[pos_i][move_j] = matrix[pos_i][move_j-1]
                matrix[pos_i][pos_j] = "."
                return (pos_i, pos_j+1)
            j += 1
            move_n += 1
        return (pos_i, pos_j)
    elif command == "<":
        j = pos_j-1
        move_n = 1
        while matrix[pos_i][j] != "#":
            if matrix[pos_i][j] == ".":
                for move_j in range(pos_j-move_n, pos_j, 1):
                    matrix[pos_i][move_j] = matrix[pos_i][move_j+1]
                matrix[pos_i][pos_j] = "."
                return (pos_i, pos_j-1)
            j -= 1
            move_n += 1
        return (pos_i, pos_j)
    

# i_0, j_0 = move(">", i_0, j_0)
# print(i_0, j_0)

# for row in matrix:
#     print("".join(row))

# print(move(">", i_0, j_0))

# for row in matrix:
#     print("".join(row))
# i_0, j_0 = move("^", i_0, j_0)


print("START")
for command in commands:
    #print()
    #print("Move: ", command)
    i_0, j_0 = move(command, i_0, j_0)
    # for row in matrix:
    #     print("".join(row))

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "O":
            total += i*100+j

print(total)