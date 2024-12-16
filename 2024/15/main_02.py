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
            strip_line = list(line.strip())
            wide_line = []
            for char in strip_line:
                if char == "#":
                    wide_line.extend(["#", "#"])
                elif char == ".":
                    wide_line.extend([".", "."])
                elif char == "@":
                    wide_line.extend(["@", "."])
                elif char == "O":
                    wide_line.extend(["[", "]"])
            matrix.append(wide_line)
        else:
            commands += line.strip()

for row in matrix:
    print("".join(row))

print(commands)

print(len(matrix))
print(len(matrix[0]))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "@":
            print(i, j)
            i_0 = i
            j_0 = j

print(i_0, j_0)

def move(command, pos_i, pos_j):
    if command == "v":
        i = pos_i+1
        move_n = 1
        can_move = True
        while matrix[i][pos_j] != "#":
            if matrix[i][pos_j] == "[":
                _, _, can_move_internal = move(command, i, pos_j+1)
                if can_move_internal == False:
                    can_move = False
            elif matrix[i][pos_j] == "]":
                _, _, can_move_internal = move(command, i, pos_j-1)
                if can_move_internal == False:
                    can_move = False
            elif matrix[i][pos_j] == ".":
                for move_i in range(pos_i+move_n, pos_i, -1):
                    matrix[move_i][pos_j] = matrix[move_i-1][pos_j]
                matrix[pos_i][pos_j] = "."
                return (pos_i+1, pos_j, can_move)
            i += 1
            move_n += 1
        can_move = False
        return (pos_i, pos_j, can_move)
    elif command == "^":
        i = pos_i-1
        move_n = 1
        can_move = True
        while matrix[i][pos_j] != "#":
            if matrix[i][pos_j] == "[":
                _, _, can_move_internal = move(command, i, pos_j+1)
                if can_move_internal == False:
                    can_move = False
            elif matrix[i][pos_j] == "]":
                _, _, can_move_internal = move(command, i, pos_j-1)
                if can_move_internal == False:
                    can_move = False
            elif matrix[i][pos_j] == ".":
                for move_i in range(pos_i-move_n, pos_i, 1):
                    matrix[move_i][pos_j] = matrix[move_i+1][pos_j]
                matrix[pos_i][pos_j] = "."
                return (pos_i-1, pos_j, can_move)
            i -= 1
            move_n += 1
        can_move = False
        return (pos_i, pos_j, can_move)
    elif command == ">":
        j = pos_j+1
        move_n = 1
        can_move = True
        while matrix[pos_i][j] != "#":
            if matrix[pos_i][j] == ".":
                for move_j in range(pos_j+move_n, pos_j, -1):
                    matrix[pos_i][move_j] = matrix[pos_i][move_j-1]
                matrix[pos_i][pos_j] = "."
                return (pos_i, pos_j+1, can_move)
            j += 1
            move_n += 1
        return (pos_i, pos_j, can_move)
    elif command == "<":
        j = pos_j-1
        move_n = 1
        can_move = True
        while matrix[pos_i][j] != "#":
            if matrix[pos_i][j] == ".":
                for move_j in range(pos_j-move_n, pos_j, 1):
                    matrix[pos_i][move_j] = matrix[pos_i][move_j+1]
                matrix[pos_i][pos_j] = "."
                return (pos_i, pos_j-1, can_move)
            j -= 1
            move_n += 1
        return (pos_i, pos_j, can_move)
    

# i_0, j_0, can_move = move("^", i_0, j_0)
# print(i_0, j_0, can_move)

# for row in matrix:
#     print("".join(row))


# print(move(">", i_0, j_0))

# for row in matrix:
#     print("".join(row))
# i_0, j_0 = move("^", i_0, j_0)

import copy
import time
print("START")
counter = 0
for command in commands:
    counter += 1
    # print(counter, "of", len(commands))
    print()
    print("Move: ", command)
    save_matrix = copy.deepcopy(matrix)
    save_i_0 = i_0
    save_j_0 = j_0
    i_0, j_0, can_move = move(command, i_0, j_0)
    print(i_0, j_0, can_move)
    if not can_move:
        # print("Can't move")
        matrix = copy.deepcopy(save_matrix)
        i_0, j_0 = save_i_0, save_j_0
    if counter % 1 == 0:
        for row in matrix:
            print("".join(row))
    time.sleep(0.2)

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "[":
            total += i*100+j

print(total)