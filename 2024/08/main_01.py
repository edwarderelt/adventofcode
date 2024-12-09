matrix = []
with open("08/input.txt", "r") as f:
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


print(matrix)
result_matrix = []
for _ in range(len(matrix)):
    result_matrix.append([0] * len(matrix[0]))


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != ".":
            #print(matrix[i][j], end="")
            for k in range(len(matrix)):
                for l in range(len(matrix[k])):
                    if k == i and l == j:
                        continue
                    if matrix[k][l] == matrix[i][j]:
                        print(matrix[k][l], end="")
                        vector_i = k - i
                        vector_j = l - j
                        new_i_1 = i - vector_i
                        new_j_1 = j - vector_j
                        if new_i_1 >= 0 and new_j_1 >= 0 and new_i_1 < len(matrix) and new_j_1 < len(matrix[0]):
                            result_matrix[new_i_1][new_j_1] = 1
                        new_i_2 = k + vector_i
                        new_j_2 = l + vector_j
                        if new_i_2 >= 0 and new_j_2 >= 0 and new_i_2 < len(matrix) and new_j_2 < len(matrix[0]):
                            result_matrix[new_i_2][new_j_2] = 1
                    else:
                        pass
                        #print(".", end="")
            #print()
        else:
            pass
            #print(".", end="")
    print()

print(result_matrix)

total_sum = 0
for i in range(len(result_matrix)):
    for j in range(len(result_matrix[i])):
        total_sum += result_matrix[i][j]

print(total_sum)