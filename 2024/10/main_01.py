matrix = []
with open("10/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(map(int, line.strip())))

print(matrix)

def get_trailheads(i, j):
    if matrix[i][j] == 9:
        return {(i, j)}
    total_trailheads = set()
    if i > 0 and matrix[i-1][j] == matrix[i][j] + 1:
        total_trailheads|=get_trailheads(i-1, j)
    if i < len(matrix)-1 and matrix[i+1][j] == matrix[i][j] + 1:
        total_trailheads|=get_trailheads(i+1, j)
    if j > 0 and matrix[i][j-1] == matrix[i][j] + 1:
        total_trailheads|=get_trailheads(i, j-1)
    if j < len(matrix[i])-1 and matrix[i][j+1] == matrix[i][j] + 1:
        total_trailheads|=get_trailheads(i, j+1)
    return total_trailheads

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            total += len(get_trailheads(i, j))
print(total)